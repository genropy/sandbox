#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    root.branch(u"Lezioni", pkg="tutor", dir="lessions")
    root.branch(u"Esempi", pkg="tutor", dir="examples")
    root.branch(u"Esercizi", pkg="tutor", dir="exercises")
