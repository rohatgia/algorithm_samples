#!/usr/bin/python

import sys

i = 252
matched = False

while(not matched):
    val = 20*i
    if((val/20).is_integer() and (val/19).is_integer() and (val/18).is_integer() and (val/17).is_integer() and (val/16).is_integer() and
       (val/15).is_integer() and (val/14).is_integer() and (val/13).is_integer() and (val/12).is_integer() and (val/11).is_integer() and
       (val/10).is_integer() and (val/9).is_integer() and (val/8).is_integer() and (val/7).is_integer() and (val/6).is_integer() and
       (val/5).is_integer() and (val/4).is_integer() and (val/3).is_integer() and (val/2).is_integer() and (val/1).is_integer()):
       print(val)
       matched = True
    i = i+1
    