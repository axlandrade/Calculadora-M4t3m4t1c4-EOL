import PySimpleGUI as sg
from sympy import *
import pyglet as pg
   
sg.ChangeLookAndFeel('Black')

elevar = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAAEnSURBVEhL7ZU9SkNBFEaf2lnY+1OqkCqbELILS7fgFtyCrZ2InYUhmwjZQ6wi+IOdot+BO4/hcudhhilS5MBhhnu/meERMtNtacmxvJdv8ndNWfMgT+UgZ/JVRpusI3sMHvYoo4U18mVFPmS0qMZ32bNjY4JAS/r9d238L0+Sxci8Gv/5ud9yJPdM5tSibLJIFE7eSrgygVqUTRaJwsgPeyQP5NJkTo1etAaLRGG8lnAjU4050MuzuUWi8Ivcl4fyy2rInBo9MvmaZJEofCnhTvoeNSDje1jEB+eSv8BY/lgtlxo9Mgur5RbxwQsJM+l7SXowkb7Xs7E3QzX+oE8bW8AF3eMPmtrYgmcbQ05ki4dvJXmpB+EwHq2at4nriMfzXG5pQdf9AYM08KZW7lAwAAAAAElFTkSuQmCC'
somar = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAAAnklEQVRIie2VUQqDMAxA38ZuoZ9zdxfxBO5IE2wvoB/ikKJJWvoh0gf5StuXltBAISM10AEemCPDAz3QWCRjgiCMEagkUZdBskUriVKe6yym/cGPQDRLVQR7YtbyNCzOQhEl81LyYbNoudMGucyNjiqMae8/92uG+4u8Yc/2aWo4SfQ1HGBlkJIf4EeewffWKqlYh5ZLEDjW4alKCmYWJUF0eN9Bza8AAAAASUVORK5CYII='
subtrair = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAAAlElEQVRIie2VQQqDMBBFX8VbpEv17kU8QT1SBZML6EJaJJBJOsxCJB/+auC/SfgwUGWoJzACAdj+dAAmoC+BLApA7AVwEmg0gHz9kkCa70p5PQc/ItAmbaHQL78xDk6qgtRqM/O4LDkly3SZF5nV/X5luD8oGGZ7CTQbgt7ScAA+2By+LreJ4zhaXgHwHMczC6kq1g6S83B51iW0xAAAAABJRU5ErkJggg=='
raiz = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABKElEQVRIie3Vvy4EURTH8Q9BswqREEKJRM0baEkkovEQOg/jARSy0WhEqOi1Eq2CwmI3/hQExcxONmPdmTum3F9yMnNzzrnfc/8zUI2aRxMdfEdaB0dYLANpVQDkrYW5EKhZA6RrhyFQ7HTtYxtXfXzPIVBs1csYxdMf/lpAt2nOWiAm03CIWqCT9LteJTlmRFtpzk0gJtNQH1Beb7hP/8ckR+ATU5jBdaDwfP/BER33+Bt4x2Xa3guMJnqNJrCCabziAqepr9L6KKjuII3ZxSom8VGQUwn0gnHMSmZipyC+8vZuYBN3+MJGRO4vFVXYPTsjeCwRn6nM9v6Psv7zU9epEdLubeRB5zWCzkLOJTyIv8Xz1sJCUSVzkkerXQHQljyehZCBSusHe3bwLV7yJ5sAAAAASUVORK5CYII='
x = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABBUlEQVRIie3VvUrEQBSG4Uc7EUHRyrUStfAKbK28AMFb8FYEe3tLCTYLVtraiHgBthY2Bkw6UYjFxCUu7OTHqWQ/OJCfb857cjiZYa6E2kKGElXPKHGN3S6QfABgOnKMYqAsAeQnrmKgIe2aFe/NxAtToCpWxQBN8i8mTjxTfUAnQoUX9f0L1rGB577gWM8fas8+PnCAJdxH1gwCVTisfUdCN9qmdDDopuE97+CfqO8wjBvXqz3X/lKsurPac4w1bOOzZU1vUCZ8/SZecVr7L1OCHrGMFTw1nsEOvrqA/v/OUCbMXcRAdwlBt7GXe3jz9yMiFwYlqpFwaBUDAIXwK7RC5uqsb8i/024J3gU9AAAAAElFTkSuQmCC'
multiplicar = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAAA4klEQVRIie2VQQ6CMBBFn14Dl2riho2nUU9oiCfQ+5iIGGGLCSwopjS1lKGRDT+ZkM6UvmGYdGBWQK2ABCiAaqAVwAXY+EAyAcC0DIhcoCQApLWzCyQp1y976wcvDFDlykKg7/lLj81P4KSeQ2JO2UpwULEYSDV/qnyoPbZ3B4FewF7Fd8AdeGgQMwExyMw+9oSIQOaX+UA6IJ9maPUBSm1dKp9Ik5bO9uNtDTIa9Lf2ToEj9hK5Yh3QZFdQERCS6wsTdAsIurqCW5oLcuyIyIB1XyYRzdDKBYCcZnj2QmZ5qwamVvGb1p0h6wAAAABJRU5ErkJggg=='
dividir = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAAAn0lEQVRIie2VQQqDMBBFn6W30GXbu4v0BO2RKjS5gC7EUgKZ6GcQF/kwqzDz5k8SBqoc1QEDEIFpZ0TgCdy3QEYBkMYItBZocICs0VsgZVy5+P4XbhLQZHUh6Ff/IianDRalgCRdhRxpvKdxtPcusm5P48jtuR/mqP4jcPpHUSmSUbBAb0fQyzp8AB98Ft+t1EnLsrSCAAgsy7MIqdqsGSPpcn9oiN9HAAAAAElFTkSuQmCC'
um = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABPUlEQVRIieXWO05CQRjF8Z92UkKJj1Lcgo0rMNElGBMXYXxtwM59oLAMxUejNnaCnYq0KhbDTQheuMPjNnqSr5mcuf95njv8Nc1FeErYxiZWsdhrf8Yj6qjiddJBFHCED3Qz6gOHvT5jqYyrCMBg3WElFrKM1gSQpFpYyoIUcDMFJKlrGct4PANIUgfDICVxG/+FJ3xm+NoopoF2IyANrPf8zQj/ThroIqPT6YA/BlRNzPN9HStp9D6VcIKNDF+/1tIaOxEj7AoJQdyMOsnH+2eUh77TQC85gFppoPscQA9poHoOoFpaY0m4ZFkbfIY9vGX43g25sISon1UE7Y+aakEIxGkhDSyMAhEiPuaODKumiN9EojIuJ4DcGuPHl6ggRH3MAWkLezJ0uWIeJ0VsCdFT8ftxUsO5cAr/kX4ABH8Kk90iIhEAAAAASUVORK5CYII='
dois =  b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABeUlEQVRIid3WP08UQRjH8Q9SeYXFXXniJcQEeSUkJpcgHaXRV0FAqXgVVISGBoz2FLQif7qz0EowFih3RgpCchSzm5zHLjN7d40+yZPsTua332dmnn2e4X+zqYQ5DbxAG3N4nI1/QwcfsIefowZRwxv00I94D2uZppI1cZgAGPZTtFIhT3A+AiT3c8zEIDUcjwHJ/UhkG99OAJL7ahmkIe3g/+B3wrwu6kWgVxHhPuazuVN4jsuI5mX+8ekB0Lrwn5TZFq7xOlvVfva+cI+mj53hwc+R6C4Gng8yzXJE0ymip5xPHzdCpYDNyNzeqKBLoRTBUgatDIpt3Q8hGR5gJQFSunXvIqI8gzbwJfPvEc1uESiW3k8LNO3E4P5qEw18xaOiKLCNq6GxlvL07mJWSftYi0RYxVdKAkAohEcTgHzCw/tAhBJ/NgbkTEKbyK2JjyNATlRofLnVhFLfTQB0hTMp3a6Uy0kdi0IqP3P3cvJe+Ad/VV3Jv223EABFYJzNAJoAAAAASUVORK5CYII='
tres = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABh0lEQVRIid3Wu09UQRTH8Q9YGLbQhI00PExssDH2dJYWJGClpbEg4U8gPPxPjLGy0khhqOjlaaNoYWIiWAHZVUoCxcyFDe69M3ehwZOczM3k/OY758ydB/+b9WXENDGNSYxjJPb/wg6W8Q4HvU6igUW0cZLwNhaippYNYz0DcNE/424uZAx7PUAK38NoCtLA1iUghW9KlHHpCiCFz5dBmvIWfh9/M+JaGOwGepEQfsedGNuPxxFapXleDH6jA/RS2Cdlti/UfRZ/8BE38ahCc4K3Fzu/JWbX6a+iZj4Rt9ONnrM+b/AMt/FQehu0i8H7K9LuZj/xSSjdCI5r6lGvdKtR8zQRd1a6zoy+ZmRzFL8HYvs7ofnSDbScEK1gSPgzJ6J2JqE5G7PzmmjiB26ViHbxOrZDeIIHFZAW7im5PhZc3RE0VzEJDeFAvCxkw/k6ltqoUJ5eIbsyronChrHWA2RbjYuvsIZwxLQyAC1hTUrLlfM4GcSU8Di579/HyQe8x2HdTK63nQKWjxpiawXKzwAAAABJRU5ErkJggg=='
quatro = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABfklEQVRIid3Wy0rbQRTH8Y/ippFWmuDKXlwUbR8m3p5AKIXuuytVoYs+gLjxKRT7CoUu2nrZeFkKJoUu2ibgRijpYv4DMfyTmUQ3euBsht/M95z/mXPmz32zsQxNDcuoYx5PivULnOIzdvB71CAqWEcbnYS3sVbsGcpm8D0D0OtHeJ4LeYbmCJDoTTxNQSo4uAEk+r7EZ9y4BUj0D/0gNXmF/yfcsMuEroVqPHy8C7SMh4PSLWyzOOBdQvcIi2WgegbkFz5m6KItlIFeZmx8gxdDgF6VLabqs4lJfC30bxP62MhgIjOyL0JNtjGbn1C5nQ2IbEmYi48xVein8WnAno4wC3E9oxPM9QliRRiohGu9JYypVF2PyxZfJ6KL/rPQ59RotQxUE5ostflKGLjnCd1fXQ3ba2uZWeX4+34QwiDcvwXIDzwYBCKM+MYNIA0Zz0S0GXwbAXJoiIcvWkUY9TkXpCXUpO/nyvk5qQoNWxf6pvfnZA+7+DNsJnfb/gNr6AwCKaWrpgAAAABJRU5ErkJggg=='
cinco = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABg0lEQVRIieXWPUtcQRQG4Mc04kIs3ELCmgQSjOJfSCe2frUWAfFfhJhI/kVaG+00ETsrS79t/CCQKitCIGG3SacWc2+46O6d2d1UyYGXC8M5533nzNxzhn/N+hJ8qpjHNMYwkq1/xwW2sIGf3Yqo4D2auI2gieUspiOr4SCB4D5O8TyV5BmuuiDJcYWnMZIKjnsgyXEkUsYPf4Ekx7t2JFVpB5+KBoby5I8KRHN4XLLb33h5D+sl/oOYbUU0UxIEP/BN+I+mMtQiMS1zflVeir3Mby3iV8RFK6LY+Wxnfq+xgFXcRGKaefJi6VJsEv34jDf42GE8uIyoK2I3ixmN+P0pXXFH5xEh10KpoJ59n0RizlotLkXUrWAYE0LX78dOJGYxT14cE1Xh+g62UXeET/gl/EOLeFWymwZeaDM+liMKO8HbEhEqmfJeSQ4xUEZEaPH1HkjqEsZEbjXsd0FyooPBl1tFaPWNBIKGcCZty5XyOBkSOvs0xj18nHzBpnAb/yO7A7ANFXiWfFsRAAAAAElFTkSuQmCC'
seis = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABfUlEQVRIid3Wz0rUURTA8U+agkO0cNqYltTCXPkI7lqGik8gPUQgmW/QozRqzyAS/t+ogSiJ40YoZrZBtbi/Xw36m9+985s2euDA5XIO3/OPey73TR4k2NSxgDd4hYns/hIn+IwGvlcNooYPaON3RNtYyXx6knHsJABu6iEmUyHPcVUBkusVnsUgNez3Acl1T6SMq/8Bkuv7bpC6tMb/xCma+FVi18JoEehtAuQTnnb4NCL2S0Wg9YjTFh7iNQ7wJcuszKdRBPoacVrEMK6FEpeVLdeTIlCsP2NCH6cy+8mEjNpVQEMYxEe8y3zmqoBipXuSZZNPHrxILd1AB+i4iN4hs7jAOTazu5mIz1HRZWy8d/FImLxBoV+HEZ+/4925Juo4w+OSCL9hIzsv+LcyiqSFl7qsj5VIhL3ockkQasKD2C9kFyNlIMIT3+wD0pSwJnIZx3YFyIEeFl8uNeGpbyUAWkJPupYr5XMyinnhczLt9udkA2v40Wsmd1v+AHaWPmYAbsl6AAAAAElFTkSuQmCC'
sete = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABcElEQVRIid2Wu0oDQRSGPy+NC1pkGyFGwUZ7O98hqEXAB/ApVqPPIQg2thpNHsHSuyBGSGmCjbdNLbGYGRjWyczZjY3+8MNy9sz5z5mZMzPw3zAm8ImBDaAKLAFz2v4MtIEW0ADeiiYRAbtACgwCTIG6HpMLZeBSIJDlHbAgFZkHegVEDHtAJSQSATcjiBheE5jGvV8QMdwZJhIjW3gpP4GSCT5pCa0D055qj4Bzh30bta5ZzABrwGH2x1kgwwRYtDiF6sOOZ0zDlfFTQMhmB7XYtYBf2yXUzyFUAyaAx4Bf3yUk3QgPeso2Bb6pCT5uCb241B3Y10G2BL5dl/FUkOEXqg1m9XfI/8RVUUuQ4T3wCqxmxg5D02WMUU3my/AYWAEOBNV8YDVsFnVBACkTX6kR6kAcVeQK1dBeVFC7pahIF8E1YVAGLgqI3JLj4jOIUEd9aIMMtE+CZ7okj5MS6mSvAsv8fJw0UT34nreSv41vAEA0zwMHzuIAAAAASUVORK5CYII='
oito = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABlElEQVRIid3WvU4UURgG4AekYUUCLAnFAiYWQoeJlRWNITYE1IZK7oDCUBnRmoS74AIAuQFjZwT8KRAaKsEYjWS3VKIUZ2bZ6Mye2XUbeZMvOZn53vOe7+f8cNnQVcCnjPuYxQRGk++fcIBtbOB7u4so4Rlq+B2xGlYSTkuoYKeAwJ/2HteLiozjpA2R1E4wFhMp4e0/iKS2J5LG5x0QSe1pnkhZscIXtSqG0sm7G4Tmca1JtGdJxDcTW8aPJv79mMv6sRVZ4Vri9xhLyXg1wtnIEjqMkB4lft9cbM7FCOcgSyhWn1fowwzuYRCvI5xaOnlPlmIOKkJtXuIXbmOkBX4dsdTdwQC+4BhXMR3h1FPX2HUfIwv5gF6hZYeFDbkb4exnCW1HSA/wGbcwha94GOHU52y8Jso4Evo/Cz+xLtToCu5iIRlnoYobcq6PFZ07GZ7kBxryvtcBkV2hnk0xJnRVuyLHClwTKSp404bIOy1cfClKwlFfLSBQFWqSm64ij5Mh4WSfxaS/HycvsInTViP5v3EOhPkT+6DGXV4AAAAASUVORK5CYII='
nove = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABlUlEQVRIid3WzUpVURTA8V9hQYe08M6yD9CgRlazpj2AZCg0SSga+AROJOsxmgeO1XqM7GtS1kAaqAmBcW6EDowa7H3gVueeve+9TWrBgsM+a+3/Wvtjrc3/JkcybFq4hSlcwtk4voUNPMMK9voNosBDtPEjoW0sRZ+eZAzrGYDf9Q0u5ELOY6cPSKU7OJeCFHg1AKTSlxLL+OgvQCp90A3SkrfxB9jPsCsxWk1+tAM0jeGGbEvciTYFZiOwm4zgZt2PtUSE89HuLubid2qpV+pA7xNOEzGT7ziMEU8mfDbqQKn9uSZUko/YxTEcT/i0+wE9iaDTOBWzO5kLGuoAfdJ8GOaEOreO65jBmQZ7wuXFr6fuXcLpG25gIdp+Fk5qk7ytG7yveRkeCxldjPZX8DXhc6+avLNNtLApnKY6+YBl4T5dxW2caMimxLgu7WMpEWEvutgQhEIoiINCXiSyRSjx2wNAtmW0iUrG8LwPyGs9NL5KCqHUlxmAUtiTrsuV8zgZFe7LFC7783HyFKv40msm/7b8BGunISkko0FoAAAAAElFTkSuQmCC'
zero = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+gvaeTAAABlElEQVRIieXWy04UQRTG8Z9oJE50NEziZrwkJkT3Lly4Z0eERzDGxGcwoK/gm+CFpTt2XlAXXNywAtxpZiZRgyguqgta6KnqmXEFJzlJV3V99T9dp/pUcdzsVI0xLcxiGjdxpejfxDpeYQFfhw2igSfoYi/jXcwXmoGsjXc1AIf9E67XhVzD9hCQ6Nu4moM08GEESPRlmWV8+h8g0ef6QVrqJX4HP2qM62AiTj5WAs3gQuJrf+ORsCTncVfIRz9r4l7VixeZCJ8V4x7ifuk5pVmoAn3OiO5gXFi2b8LP3spo1qtAvYyoiclDbfie0PTi5OUc7VXRS/YTZ0vt+LyT0OzPWQZ9yYAuO6hnu8KuuoSLCc3+ZimD1jKg20Uwb/AavzCV0axWdT6QztESzuB04U2sZDRxd/5zTLSw4SDJVbaMRfwRtnY7MbaDG/ocH/OZCAfxx4kgNIqoR4W8x7kUiFDit0aAbKlxTERr4+0QkI8GOPiiNYRS36kB6Ag56btcdS4nE0Jln8YtRy8nL/FcqH8nyP4CQk4VezPH/mkAAAAASUVORK5CYII='
ponto = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAAEvSURBVEhL7dTNSgJRGMbxKTcZCkEkRITbQJduXAm1bOu2a/EWXLT2GlqIG111A0KhqxQXbfogiKwIy/o/nhkI5ng8ziJazAM/5h0/eM+cmXeCNGn+PBvh0ZUMjnCMCg6gjNFDG+/4RuLkcYYL3OAZn6EnXOEcRWhBiaI/qsklXqEV2zyiiX347FAsJehKXE0id6hDO2DNZni05QRlbC/O3CngFLuLM0tcjXTj90zplSp2TBmPq5H23Odqohxiy5TxuBqtm3l4tMbVaIIXU3plhDdTxuNq1MWtKb3SwYMp14vuj4ZRc2J7pH8bQk9ooqHV8GniNYyaE1sDUZMalj4IyqoVTNHHNbT/WehKZxighQb0/QeWxueVod/koGHUnEQrV2Pdk3t86YM0af5TguAHWspKWl3CUa0AAAAASUVORK5CYII='
par1 = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAALiMAAC4jAXilP3YAAAJ/SURBVEhL3VW7bhNBFL3rdRCQUAQJIgoXREQUgFwRkyaF6cInUPEDLujIP7iBdPyAa38DBgnRIHeAUjhygVAMBPESdpZz7szuzHhnY9c50tmdx7333LkzOyvnDol952D/MrgpUl+XdLoiMx2PIgVn9glk4F/wGByBv+2YwhdCewMin3fRfgreBVc5kYPGhWcZpyBFXoMvwXdgIGZxbQ2PJ+BPkE4wSGhUIgTPGp+Ch2ALvACWsAMeIu3KQAFhFx03ZAkPwA1QUbNv4jZ4nWa0rALLt6iGwAp4D7ykPcAXugpyZw00YgUqRIxLnkrCQ1XE94V+YNqFKFq+omcQScTMxS18oSPsTuQwO222H7Ra0mw2w2EfRfiM1WEJFb7QPxyyCnfj3W635dn+vqxd4QGtgItwEWT5FL6QGoWFsn095SJ7j/ak1+vJ4NVA+1WwMeqWilAIJhrSWubnnI/t7ZZs3dqSfr+vc2fBpBViTsia5Jb5G4K1tCaTyURmU36PJhM+bU4LMSdUhgaC4NFoJGk9lZubuAZtBnzmuSxCIOTydMgDjcdjGQ6H0ul07IhBaUUVS/SEUg0as8sTOHj+QhqNhnS7XR3hWGlFSyzxIRxPEJSmEfLoJVmSGMZtcH7cHfgRvA8q/NJhMjulRRzGP8OnRvrwq+BN8dSQCl+IN+6XoHSxOkbgYhcOHPoKftce4Avhp5UMcP8zC+PrJc4Qi3TdjmmMN+CJdn3cMNfFLoJ9gOEftPHzM/uC9rLkD5O+78E7YHEzuLViKdhI/j/4C38MNjG7CvfIQjjEuAEognIlbzHXQ/sTyO1QzAdhnzfuOkjR4DtbAizZL/CbbZ9biPwHubLUK4hnuTsAAAAASUVORK5CYII='
par2 = b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAALiMAAC4jAXilP3YAAAJ/SURBVEhL3Za/bhNBEMbniEEETAGyiWgcjBSQDIgKoUSyG57ANRWvwEu4ckdoeAHeAdwZkBANEmkAUUBjhBBOrPDP2Mf3ze7e7d3uobjNJ/2ys3MzO/vHtxc5dkps68T+GXAFnAcnQa41sNA/2nWynhTNb/ANfAI/AX0qv1AiGyjyRXqwH4Ab4CwfHEUYaIlRWeRFTeTxX5HXsAvFVE2ROpr74BAsAQNSjGDao4Ma8hHcAadAoG0MyoBY8qpwCx+CDaA6YVvqGkIuWrug8kGGCiJ4tjfBuvagrBCMC4kkPNdAnGJ1NT5gBNo8hhZ/VP74RjiUWSqpjpknOANtrBq6PELjRYDJdioE+1v3GZjfbZbgjFTO1euys7MtrVbL+oxSN4dQ3J3s9fALzQHzolqr1aTX68lgMJB2u22csQr5AKcBt0/lF1JFZ4fk6XQqu7uPZP5nLv1+P39QTnD9RPA6KaqgUHFrrW2TZ7OZPBs9lWYTb50qOi0onECkkB9RjE6SVBaLpTQajcJ0QoUTiBSqFn+Tm5c3ZTKZVK5FFZnFSoU6nY50u10Zj8fWA8WWhlmU3WGhINE4tq5uyXA4lL23ezIajdSnKi8N4cz434rvggPAGAUJma19HBLxfTnOnz1/D24Dlb8iPuStnQmjWssoxSGRoteJ6bY1AbzFicovxBv3qzGt7I1UVuaNV2QAQ76Dfe1DfiF+tJ4DzILLd6Pgqs2skuLzYCBX8hLwKEq6pNcFv67vwC9Elz5+OB/Xr4Y5yJU3uOauo81uBm+SHCfh94Of8HvgFuCnPFhIhViE2/UKPAEfAI9DVR6Efd64/MeERVd6zyBu2Q8wtfaxlcg/PE/QjR9ucCgAAAAASUVORK5CYII='

left_column = [
    [sg.Text('Expressão: '), sg.InputText("", key='expressao', size=(45,1))],
    [sg.HorizontalSeparator(color='black')],
    [sg.Button('Expressão Simples', key='simples'), sg.Button('Equação', key='equacao'), sg.Button('Inequação', key='inequacao'), sg.Button('Limite', key='limite'), 
    sg.Button('Derivada', key='derivada'), sg.Button('Integral Ind.', key='integral_ind')],
    [sg.Output(size=(54,20), key='output')],
    [sg.HorizontalSeparator()],
    [sg.Button('', image_data = sete, key = '7'), sg.Button('', image_data = oito, key = '8'), sg.Button('', image_data = nove, key = '9'), 
     sg.Button('', image_data = subtrair, key = '-'), sg.Button('',image_data = dividir, key = '/')],
    [sg.Button('', image_data = quatro, key = '4'), sg.Button('', image_data = cinco, key = '5'), sg.Button('', image_data = seis, key = '6'), 
     sg.Button('', image_data = somar, key = '+'), sg.Button('', image_data = multiplicar, key = '*'),],
    [sg.Button('', image_data = um, key = '1'), sg.Button('', image_data = dois, key = '2'), sg.Button('', image_data = tres, key = '3'), 
     sg.Button('', image_data = ponto, key = '.'), sg.Button('', image_data = elevar, key = '^'),],
    [sg.Button('', image_data = zero, key = '0'), sg.Button('Limpar', key = 'limpar')],
    [sg.Text("Símbolos: "), sg.Button('', image_data = x, key = 'X'), sg.Button('', image_data = raiz, key = 'raiz'), sg.Button('', image_data = par1, key = '('), 
     sg.Button ('', image_data  = par2, key = ')')],
    [sg.Text("Versão: Beta 2.0")],
    [sg.Text('Programa desenvolvido por Axl Andrade (UFRRJ-UNESA)')]
]

right_column = [
    [sg.Button('Área do quadrado', key = 'quadrado')],
    [sg.Button('Área do triângulo', key = 'triangulo')],
    [sg.Button('Área do retângulo', key = 'retangulo')],
    [sg.Button('Área do Círculo', key = 'circulo')]
]

layout = [[sg.Column(left_column, element_justification='c'), sg.VSeparator(), sg.Column(right_column, element_justification='c')]]

window = sg.Window('M4t3m4t1c4', layout, element_padding=(2,2), resizable=True)

while True:
    event, values = window.read()

    if event == '7':
        expressao = values['expressao']
        expressao = values['expressao'] + str(7)
        window.FindElement('expressao').Update(expressao)
        
    if event == '8':
        expressao = values['expressao']
        expressao = values['expressao'] + str(8)
        window.FindElement('expressao').Update(expressao)
        
    if event == '9':
        expressao = values['expressao']
        expressao = values['expressao'] + str(9)
        window.FindElement('expressao').Update(expressao)
        
    if event == '4':
        expressao = values['expressao']
        expressao = values['expressao'] + str(4)
        window.FindElement('expressao').Update(expressao)
        
    if event == '5':
        expressao = values['expressao']
        expressao = values['expressao'] + str(5)
        window.FindElement('expressao').Update(expressao)
        
    if event == '6':
        expressao = values['expressao']
        expressao = values['expressao'] + str(6)
        window.FindElement('expressao').Update(expressao)
        
    if event == '1':
        expressao = values['expressao']
        expressao = values['expressao'] + str(1)
        window.FindElement('expressao').Update(expressao)
        
    if event == '2':
        expressao = values['expressao']
        expressao = values['expressao'] + str(2)
        window.FindElement('expressao').Update(expressao)
        
    if event == '3':
        expressao = values['expressao']
        expressao = values['expressao'] + str(3)
        window.FindElement('expressao').Update(expressao)
        
    if event == '0':
        expressao = values['expressao']
        expressao = values['expressao'] + str("0")
        window.FindElement('expressao').Update(expressao)
        
    if event == '-':
        expressao = values['expressao']
        expressao = values['expressao'] + str("-")
        window.FindElement('expressao').Update(expressao)
        
    if event == '+':
        expressao = values['expressao']
        expressao = values['expressao'] + str("+")
        window.FindElement('expressao').Update(expressao)
        
    if event == '.':
        expressao = values['expressao']
        expressao = values['expressao'] + str(".")
        window.FindElement('expressao').Update(expressao)
        
    if event == '/':
        expressao = values['expressao']
        expressao = values['expressao'] + str("/")
        window.FindElement('expressao').Update(expressao)
        
    if event == '*':
        expressao = values['expressao']
        expressao = values['expressao'] + str("*")
        window.FindElement('expressao').Update(expressao)
        
    if event == '^':
        expressao = values['expressao']
        expressao = values['expressao'] + str("**")
        window.FindElement('expressao').Update(expressao)
        
    if event == 'X':
        expressao = values['expressao']
        expressao = values['expressao'] + str("x")
        window.FindElement('expressao').Update(expressao)
        
    if event == 'raiz':
        expressao = values['expressao']
        
        layout = [[sg.Text("Digite o número que você deseja na raiz"), sg.InputText(key = 'x_raiz')],
                  [sg.Submit('Confirmar'), sg.Submit('Cancelar')]
                  ]
        
        popup_xraiz = sg.Window('Número da raiz', layout)
        
        event, values = popup_xraiz.read()
        
        x_raiz = values['x_raiz']
        popup_xraiz.close()
        
        expressao = expressao + str("sqrt(") + str(x_raiz) + str(")")
        window.FindElement('expressao').Update(expressao)
        
    if event == '(':
        expressao = values['expressao']
        expressao = values['expressao'] + str("(")
        window.FindElement('expressao').Update(expressao)
        
    if event == ')':
        expressao = values['expressao']
        expressao = values['expressao'] + str(")")
        window.FindElement('expressao').Update(expressao)
        
    if event == 'limpar':
        expressao = values['expressao']
        expressao = ""
        output = ""
        window.FindElement('expressao').Update(expressao)
        window.FindElement('output').Update(output)
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'simples':
        simples = values['expressao']
        sol = eval(simples)
        init_printing()
        print("Sua solução é:\n")
        pprint(sol)
        print("\n")
        
    if event == 'equacao':
        x = symbols('x')
        equacao = values['expressao']
        sol = solveset(equacao)
        init_printing()
        print("Sua solução é:\n")
        pprint(sol)
        print("\n")
        
    if event == 'inequacao':
        x = symbols('x')
        inequacao = values['expressao']
        sol = solveset(inequacao, x, domain=S.Reals)
        init_printing()
        print("Sua solução é:\n")
        pprint(sol)
        print("\n")
        
    if event == 'limite':
        expr = values['expressao']
        
        layout = [[sg.Text('Digite aqui o valor para qual x se aproxima')],
                  [sg.InputText(key='x_tende')],
                  [sg.Submit(), sg.Cancel()]]
    
        popupx = sg.Window('De qual valor x se aproxima', layout)
    
        event, values = popupx.read()
        x_apr = values['x_tende']
        popupx.close()
        
        x = symbols('x')
        
        limite_expr = limit(expr, x, x_apr)
        init_printing()
        print("Seu limite vale:\n")
        pprint(limite_expr)
        print("\n")
    
    if event == 'derivada':
        x = symbols('x')
        expr = values['expressao']
        derivada_expr = diff(expr)
        init_printing()
        print("Sua derivada retorna:\n")
        pprint(derivada_expr)
        print("\n")
    
    if event == 'integral_ind':
        x = symbols('x')
        expr = values['expressao']
        integral_expr = integrate(expr, x)
        init_printing()
        print("Sua integral retorna: ")
        pprint(integral_expr)
        print("\n")

    if event == 'quadrado':

        layout = [[sg.Text('Digite o valor do lado do seu quadrado')],
            [sg.InputText(key = 'lado')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]]

        popupq = sg.Window('Área do quadrado', layout)
        while True:
            event, values = popupq.read()

            if event == 'Cancelar' or event == None:
                break
            
            if event == 'Confirmar':
                lado_q = values['lado']
                area = int(lado_q)**2
                init_printing()
                print("Sua área vale:\n", area)
                print("\n")
                break
            
        popupq.close()

    if event == 'triangulo':

        layout = [[sg.Text('Insira aqui a base e a altura do seu triângulo')],
                  [sg.Text('Base:'), sg.InputText(key = 'base')],
                  [sg.Text('Altura'), sg.InputText(key = 'altura')],
                  [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]]

        popupt = sg.Window('Área do triângulo', layout)
        while True:
            event, values = popupt.read()
            
            if event == 'Cancelar' or event == None:
                break
            
            if event == 'Confirmar':
                base_t = values['base']
                alt_t = values['altura']
                area = (int(base_t) * int(alt_t))/2
                init_printing()
                print("Sua área vale:\n", area)
                print("\n")
                break
            
        popupt.close()

    
    if event == 'retangulo':
        
        layout = [[sg.Text('Insira aqui a base e a altura do seu retângulo')],
                  [sg.Text('Base:'), sg.InputText(key = 'base')],
                  [sg.Text('Altura'), sg.InputText(key = 'altura')],
                  [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]]
        
        popupr = sg.Window('Área do retângulo', layout)
        while True:
            event, values = popupr.read()
            
            if event == 'Cancelar' or event == None:
                break
            
            if event == 'Confirmar':
                base_r = values['base']
                alt_r = values['altura']
                area = (int(base_r) * int(alt_r))
                init_printing()
                print("Sua área vale:\n", area)
                print("\n")
                break  
        
        popupr.close()
        
    if event == 'circulo':

        layout = [[sg.Text('Digite o valor do raio do seu círculo')],
            [sg.InputText(key = 'raio')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]]

        popupc = sg.Window('Área do círculo', layout)
        while True:
            event, values = popupc.read()

            if event == 'Cancelar' or event == None:
                break
            
            if event == 'Confirmar':
                raio = values['raio']
                area = 3.14 * int(raio)**2
                init_printing()
                print("Sua área vale:\n", area)
                print("\n")
                break
            
        popupc.close()   

window.close()
