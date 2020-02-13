#!/usr/bin/env python
# -*- coding: utf-8 -*-

class stopType():
  feuer = 0
  kanto = 0
  relaxo = 0
  kaefer = 0
  drache = 0
  kampf = 0
  flug = 0
  pflanze = 0
  boden = 0
  normal = 0
  gift = 0
  psycho = 0
  gestein = 0
  wasser = 0
  karpador = 0
  eis = 0
  elektro = 0
  stahl = 0
  geist = 0
  unlicht = 0
  fee = 0
  boss = 0

  Sfeuer = ""
  Skanto = ""
  Srelaxo = ""
  Skaefer = ""
  Sdrache = ""
  Skampf = ""
  Sflug = ""
  Spflanze = ""
  Sboden = ""
  Snormal = ""
  Sgift = ""
  Spsycho = ""
  Sgestein = ""
  Swasser = ""
  Skarpador = ""
  Seis = ""
  Selektro = ""
  Sstahl = ""
  Sgeist = ""
  Sunlicht = ""
  Sfee = ""
  Sboss = ""

  standard = 0
  gletscher = 0
  moos = 0
  magnet = 0

  Sstandard = ""
  Sgletscher = ""
  Smoos = ""
  Smagnet = ""

    ####Rocketstops
  def typ4(self):
    self.kanto +=1
    self.Skanto = "\U00002b55 " + str(self.kanto) + " "
    return " \U00002b55 Kanto Starter"
  def typ5(self):
    self.relaxo +=1
    self.Srelaxo ="\U0001f6cf " + str(self.relaxo) + " "
    return " \U0001f6cf Relaxo"
  def typ7(self):
    self.kaefer +=1
    self.Skaefer ="\U0001f41B " + str(self.kaefer) + " "
    return " \U0001f41B K\U000000e4fer"
  def typ12(self):
    self.drache +=1
    self.Sdrache ="\U0001f409 " + str(self.drache) + " "
    return " \U0001f409 Drache"
  def typ16(self):
    self.kampf +=1
    self.Skampf ="\U0001f94a " + str(self.kampf) + " "
    return " \U0001f94a Kampf"
  def typ18(self):
    self.feuer +=1
    self.Sfeuer ="\U0001f525 " + str(self.feuer) + " "
    return " \U0001f525 Feuer"
  def typ20(self):
    self.flug +=1
    self.Sflug ="\U0001f985 " + str(self.flug) + " "
    return " \U0001f985 Flug"
  def typ23(self):
    self.pflanze +=1
    self.Spflanze ="\U0001f33f " + str(self.pflanze) + " "
    return " \U0001f33f Pflanze"
  def typ25(self):
    self.boden +=1
    self.Sboden ="\U0001f5fb " + str(self.boden) + " "
    return " \U0001f5fb Boden"
  def typ31(self):
    self.normal +=1
    self.Snormal ="\U0001f401 "+ str(self.normal) + " "
    return " \U0001f401 Normal"
  def typ32(self):
    self.gift +=1
    self.Sgift ="\U0001f577 " + str(self.gift) + " "
    return " \U0001f577 Gift"
  def typ35(self):
    self.psycho +=1
    self.Spsycho ="\U0001f52e " + str(self.psycho) + " "
    return " \U0001f52e Psycho"
  def typ37(self):
    self.gestein +=1
    self.Sgestein ="\U0001f311 "+ str(self.gestein) + " "
    return " \U0001f311 Gestein"
  def typ38(self):
    self.wasser +=1
    self.Swasser ="\U0001f4a7 " + str(self.wasser) + " "
    return " \U0001f4a7 Wasser"
  def typ39(self):
    self.karpador +=1
    self.Skarpador ="\U0001f420 " + str(self.karpador) + " "
    return " \U0001f420 Karpador"
  def typ49(self):
    self.elektro +=1
    self.Selektro ="\U000026a1 "+ str(self.elektro) + " "
    return " \U000026a1 Elektro"
  def typ48(self):
    self.geist +=1
    self.Sgeist  ="\U0001f47b "+ str(self.geist) + " "
    return " \U0001f47b Geist"
  def typ97(self):
    self.fee +=1
    self.Sfee  ="\U0001f496 "+ str(self.fee) + " "
    return " \U0001f496 Fee"
  def typ98(self):
    self.stahl +=1
    self.Sstahl  ="\U00002699 "+ str(self.stahl)  + " "
    return " \U00002699 Stahl"
  def typ99(self):
    self.unlicht +=1
    self.Sunlicht   ="\U0001f317 "+ str(self.unlicht)  + " "
    return " \U0001f317 Unlicht"
  def typ26(self):
    self.eis +=1
    self.Seis  ="\U00002744  "+ str(self.eis)  + " "
    return " \U00002744 Eis"

  ####Boose
  def typ41(self):
    self.boss +=1
    self.Sboss ="\U0001f63a "+str(self.boss) + " " 
    return " \U0001f63a Cliff "
  def typ42(self):
    self.boss +=1
    self.Sboss ="\U0001f997 "+str(self.boss) + " " 
    return " \U0001f997 Arlo "
  def typ43(self):
    self.boss +=1
    self.Sboss ="\U00002603 "+str(self.boss) + " " 
    return " \U00002603 Sierra "
  def typ44(self):
    self.boss +=1
    self.Sboss ="\U0001f454 "+str(self.boss) + " "
    return " \U0001f454 Giovanni\U00002753"

  ####Lockmodule
  def typ501(self):
    self.standard +=1
    self.Sstandard = "\U0001F39F " + str(self.standard)
    return "\U0001F39F Normales Lockmodul"
  def typ502(self):
    self.gletscher +=1
    self.Sgletscher = "\U00002744 " + str(self.gletscher)
    return "\U00002744 Gletscher Lockmodul"
  def typ503(self):
    self.moos +=1
    self.Smoos = "\U0001f4c3 " + str(self.moos)
    return "\U0001f4c3 Moos Lockmodul"
  def typ504(self):
    self.magnet +=1
    self.Smagnet = "\U0001F9F2 " + str(self.magnet)
    return "\U0001F9F2 Magnet Lockmodul"

  def getType(self,value):
    switch = {
      4: self.typ4,
      5: self.typ5,
      7: self.typ7,
      12:self.typ12,
      16:self.typ16,
      18:self.typ18,
      20:self.typ20,
      23:self.typ23,
      25:self.typ25,
      31:self.typ31,
      32:self.typ32,
      35:self.typ35,
      37:self.typ37,
      38:self.typ38,
      39:self.typ39,
      48:self.typ48,
      49:self.typ49,
      97:self.typ97,
      98:self.typ98,
      99:self.typ99,
      26:self.typ26,
      41:self.typ41,
      42:self.typ42,
      43:self.typ43,
      44:self.typ44,
      501:self.typ501,
      502:self.typ502,
      503:self.typ503,
      504:self.typ504
    }
    typ = switch.get(value,lambda: str(value))
    return typ()