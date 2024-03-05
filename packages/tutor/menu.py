#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    root.webpage(u"Local Handbooks", filepath="/sandbox/local_handbooks")
    root.branch(u"Lezioni", pkg="tutor", dir="lessons")
    root.branch(u"Esempi", pkg="tutor", dir="examples")
    root.branch(u"Esercizi", pkg="tutor", dir="exercises")
