#!/usr/bin/python


from pisi.actionsapi import pisitools

WorkDir = "MediterraneanNight-2.03"

def install():
    for theme in ["MediterraneanDark", "MediterraneanDarkest", "MediterraneanGrayDark", \
                  "MediterraneanLight", "MediterraneanLightDarkest", "MediterraneanNight", \
                  "MediterraneanNightDarkest", "MediterraneanTribute", "MediterraneanTributeBlue", \
                  "MediterraneanTributeDark", "MediterraneanWhite", "MediterraneanWhiteNight"]:
        pisitools.insinto ("/usr/share/themes", theme)
