#!/usr/bin python3

import os
from notion.client import NotionClient


def main():
  generator = Generator()
  generator.generate()


class Generator(object):


  def __init__(self):
    self.listNumber = 0
    self.BLOG_LINK = 'https://www.notion.so/gaohongyuan/841cec94d55c4e5a979bd3fa3e983e1e?v=d8b2e778fc514d2a837f4160b4bdeaf6'
    self.TOKEN = '300ab9640b6e3d4ec2cc8da0878cdecaaf6219aeafe0815a72a97e07032cc8c7a0f1187eebb6d9170abf96749e6d6d9f753fb774e881e783f31db333815a4a7edc823cfc09ce4a0157ed0c0b53cf'
    self.DIR = '/home/gaohongyuan/Dropbox/Public/source/blog/content'
    # self.DIR = '.'
    self.POST_NOTION_DIR = '{}/post_notion'.format(self.DIR)
    self.POST_NOTION_NEW_DIR = '{}/post_notion_new'.format(self.DIR)
    self.POST_DIR = '{}/post'.format(self.DIR)
    self.BLOG_DIR = '/home/gaohongyuan/Dropbox/Public/sites/blog'
    self.DIRS = '/home/gaohongyuan/Dropbox/Public/source/blog'

  def generate(self):
    posts = self.get_posts()
    os.system('mkdir {}'.format(self.POST_NOTION_NEW_DIR))
    for post in posts:
      if post.published:
        header = self.generate_header(post)
        markdown_text = self.generate_content(post)
        md_file = open('{}/{}.md'.format(self.POST_NOTION_NEW_DIR, post.filename), 'w')
        md_file.write(header)
        md_file.write(markdown_text)
        md_file.close()

    if (self.has_diff()):
      # self.copy()
      # self.deploy()
      return

  def has_diff(self):
    return os.system('diff -q {} {}'.format(self.POST_NOTION_DIR, self.POST_NOTION_NEW_DIR)) != 0
  
  def copy(self):
    os.system('rm -r {}'.format(self.POST_NOTION_DIR))
    os.system('mv {} {}'.format(self.POST_NOTION_NEW_DIR, self.POST_NOTION_DIR))
    os.system('cp {}/*.md {}/'.format(self.POST_NOTION_DIR, self.POST_DIR))
    # os.system('rm -r {}'.format(self.POST_NOTION_NEW_DIR))
    return

  def deploy(self):
    os.system('hugo -s {} -d {}'.format(self.DIRS, self.BLOG_DIR))
    return


  def get_posts(self):
    # Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
    client = NotionClient(token_v2=self.TOKEN)

    # Access a database using the URL of the database page or the inline block
    return client.get_collection_view(self.BLOG_LINK).collection.get_rows()

  def generate_header(self, post):
    date_string = post.date.start.strftime('date = "%Y-%m-%dT00:00:00-08:00"')
    title_string = 'title = "{}"'.format(post.title) 
    summary_string = 'summary = "{}"'.format(post.summary) 
    category_string = 'categories = "{}"'.format(post.category) 
    return '\n'.join(['+++', '', date_string, title_string, summary_string, category_string, '', '+++', '', ''])

  def generate_content(self, post):
    # print(post.children)
    # print(post.children[26].children)
    lines = []
    self.append_lines(lines, post.children, 1)
    return ''.join(lines)

  def append_lines(self, lines, current, layer):
    for block in current:
      lines.append(self.generate_line(block, layer))
      self.append_lines(lines, block.children, layer + 1)



  def generate_line(self, block, layer):
    block_type = block.type
    # print(block_type)
    prefix = ''
    suffix = '\n\n'

    if block_type == 'image':
      prefix = '\n' * int(self.reset_list_number()) + '![IMAGE]('
      suffix = ')\n\n'
      return prefix + block.source + suffix
    if block_type == 'text':
      prefix = '\n' * int(self.reset_list_number()) + ''
    elif block_type == 'header':
      prefix = '\n' * int(self.reset_list_number()) + '# '
      self.listNumber = 0
    elif block_type == 'sub_header':
      prefix = '\n' * int(self.reset_list_number()) + '## '
      self.listNumber = 0
    elif block_type == 'sub_sub_header':
      prefix = '\n' * int(self.reset_list_number()) + '### '
      self.listNumber = 0
    elif block_type == 'code':
      prefix = '\n' * int(self.reset_list_number()) + '```\n'
      suffix = '\n```\n\n'
      self.listNumber = 0
    else:
      self.listNumber += 1
      prefix = self.get_prefix_for_list(block_type, layer)
      suffix = '\n'
    return prefix + block.title + suffix

  def get_prefix_for_list(self, block_type, layer):
    if block_type == 'bulleted_list':
      return '  ' * (layer - 1) + '* '
    if block_type == 'numbered_list':
      return '  ' * (layer - 1) + str(self.listNumber) + '. '
    # toggle / quote
    return '> '

  def reset_list_number(self):
    success = self.listNumber > 0
    self.listNumber = 0
    return success




if __name__ == "__main__":
  main()
