#!/bin/bash


txt2tags -t man -o wsgid.8 wsgid.t2t
bzip2 -f9 wsgid.8
