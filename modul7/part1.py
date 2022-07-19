#objects

# class Keyboard:
#     typed = ''             #Class variable
#     shift_pressed = False  #Class variable
#
#     def press_shift(self):
#         self.shift_pressed = True
#
#     def release_shift(self):
#         self.shift_pressed = False
#
#     def press_a(self):
#         if self.shift_pressed:
#             self.typed += 'A'
#         else:
#             self.typed += 'a' # <- learn self
#
#     def how_is_self(self):
#         print(id(self))
#
# keyboard = Keyboard()
#
# print(type(keyboard))
# print(f'valoarea este: {keyboard.typed}')
# keyboard.press_a()
# print(f'noua valoarea este: {keyboard.typed}')
# keyboard.press_a()
# print(f'noua noua valoarea este: {keyboard.typed}')
# keyboard.how_is_self()
# print(id(keyboard))
#
# #new keyboard
#
# keyboard1 = Keyboard()
# print(f'new keyboard - valoarea este: {keyboard1.typed}')
# keyboard1.press_shift()
# keyboard1.press_a()
# keyboard1.release_shift()
# print(f'new keyboard - noua valoarea este: {keyboard1.typed}')


#gaina

# class Gaina:
#     neutral = """
#                                            _
#                                    .-.  .--''` )
#                                 _ |  |/`   .-'`
#                                ( `\      /`
#                                _)   _.  -'._
#                              /`  .'     .-.-;
#                              `).'      /  \  "
#                             (`,        \_o/_o/__
#                              /           .-''`  ``'-.
#                              {         /` ,___.--''`
#                              {   ;     '-. \ |
#            _   _             {   |'-....-`'.\_|
#           / './ '.           \   \          `"`
#        _  \   \  |            \    |
#       ( '-.J     \_..----.._ __)   `\--..__
#      .-`                    `        `\    ''--...--.
#     (_,.--""`/`         .-             `\       .__ _)
#             |          (                 }    .__ _)
#             \_,         '.               }_  - _.'
#                \_,         '.            } `'--'
#                   '._.     ,_)          /
#                      |    /           .'
#                       \   |    _   .-'
#                        \__/;--.||-'
#                         _||   _||__   __
#                  _ __.-` "`)(` `"  ```._)
#                 (_`,-   ,-'  `''-.   '-._)
#                (  (    /          '.__.'
#                 `"`'--'  """
#
#     cot_codac = False
#
#     def cot_codac_once(self):
#         self.cot_codac = True
#
#     def cot_codac_nope(self):
#         self.cot_codac = False
#
#     def lay_egg(self):
#         if self.cot_codac == False:
#             self.neutral = """
#               xx
#              / .|_
#             /(_)_< --- cack cack, made an egg !
#            /  (
#   ((____.-'    )
#    \          /
#     \-.-.-'` /
#   _  \______/
#  (_)   _|_\_  """
#
#
# gaina = Gaina()
#
# print(type(gaina))
# print(f'gaina calma: {gaina.neutral}')
# gaina.lay_egg()
# print(f'gaina quack: {gaina.neutral}')
# gaina.lay_egg()






