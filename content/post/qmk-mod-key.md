+++
categories = "Tech"
date = "2019-05-22T00:00:00+00:00"
title = "An Optimization of QMK Mod-tap (Layer-tap) for Fast Typists"
summary = "The default mod-tap feature of QMK doesn't support fast typing well. In this post I wrote a customized function to optimize its performance."
+++

**The code doesn' work as expected. Please refer to `IGNORE_MOD_TAP_INTERRUPT` and `PERMISSIVE_HOLD` [here](https://github.com/qmk/qmk_firmware/blob/master/docs/config_options.md) for possible workarounds.**


[QMK](http://qmk.fm) is the most powerful and popular keyboard firmware in custimzed mechanical keyboard community. It allows you to can write C code to set macros to any key, which makes it highly playable.

Apart from programming, QMK has quite a lot of pre-set quantum keys. An important category of them is mod-tap keys. That means, when you tap the key, it prints a normal output, such as a letter, digit or any other key on the keyboard; when you hold it, it works like a mod key, such as Control, Alt, Shift or Win (Command/Super). That's particually useful for mini keyboards (40% layout, for example), where keys are highly reused.

However, the performance of mod-tap may not meet the need of fast typing. For example, if the mod-tap key is Control(A), and you press Control(A) and C fast, it actually prints "AC" on the screen, but not sends a Control + C combination. The same thing happens on layer-tap key.

I haven't read the source code of mod-tap keys, but with programming, we can avoid this issue completely.

{{< highlight c "linenos=inline">}}
#include QMK_KEYBOARD_H

bool lctl_other_key_pressed = false;
uint16_t lctl_hold_timer = 0;

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
  switch (keycode) {
    // Left control. Can be changed to any modifier, or MO({LAYER_NUM}) for layer-taps.
    case KC_LCTL:
      if (record->event.pressed) {
        // Records press time.
		lctl_hold_timer = timer_read();
        // At the beginning, no other key is pressed.
		lctl_other_key_pressed = false;
      } else if (timer_elapsed(lctl_timer) < 500 && !space_other_key_pressed) {
        // Sends out 'A' if the key is held for less than 0.5s and no other key was pressed during the period. 
		tap_code(KC_A);
	  }
      break;
	default:
      // Another key is pressed.
      lctl_other_key_pressed = true;
  }
  return true;
};
{{< / highlight >}}

In this piece of code, we set the keycode of the mod-tap key to a normal Control key. It ensures it works perfectly as a mod key. Then we attach another event to this key when it is released - we sends a normal letter, which is the "tap" part of mod-tap. Tap is only triggerred when the key was held shortly and no other key is pressed before release. This way, even fast typists can enjoy mod-tap keys happily.

I'm not sure if the current behavior of mod-tap is expected by QMK developer, but I will do some investigation on it and see if I can make the solution general to the default mod-tap implementation.
