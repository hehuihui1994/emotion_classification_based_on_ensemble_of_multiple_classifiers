#!/usr/bin/env cpp
# -*- coding: utf-8 -*-
# @Date    : 2016-07-10 21:04:27
# @Author  : JieJ (jiej1992@163.com)

def get_doc_unis_list(doc_str_list):
    '''generate unigram language model for each segmented instance'''
    unis_list = [x.strip().split() for x in doc_str_list]
    return unis_list

def get_doc_bis_list(doc_str_list):
    '''generate bigram language model for each segmented instance'''
    unis_list = get_doc_unis_list(doc_str_list)
    doc_bis_list = []
    for k in range(len(doc_str_list)):
        unis = unis_list[k]
        if len(unis) == 0:
            doc_bis_list.append([])
            continue
        unis_pre, unis_after = ['<bos>'] + unis, unis + ['<eos>']
        doc_bis_list.append([x + '<w-w>' + y for x, y in zip(unis_pre, unis_after)])
    return doc_bis_list

def get_doc_triple_list(doc_str_list):
    '''generate triple-gram language model for each segmented instance'''
    doc_unis_list = get_doc_unis_list(doc_str_list)
    doc_bis_list = get_doc_bis_list(doc_str_list)
    doc_triple_list = []
    for k in range(len(doc_str_list)):
        unis = doc_unis_list[k]
        bis = doc_bis_list[k]
        if len(bis)<=2:
            doc_triple_list.append([])
            continue
        pre, after = bis[:-1], unis[1:] + ['<eos>']
        doc_triple_list.append([x + '<w-w>' + y for x, y in zip(pre, after)])
    return doc_triple_list

def get_doc_quat_list(doc_str_list):
    '''generate triple-gram language model for each segmented instance'''
    doc_unis_list = get_doc_unis_list(doc_str_list)
    doc_bis_list = get_doc_bis_list(doc_str_list)
    doc_triple_list = get_doc_triple_list(doc_str_list)
    doc_quat_list = []
    for k in range(len(doc_str_list)):
        unis = doc_unis_list[k]
        bis = doc_bis_list[k]
        triple = doc_triple_list[k]
        if len(triple)<=2:
            doc_quat_list.append([])
            continue
        pre, after = ['<bos>'] + unis[:-2], triple[1:]
        doc_quat_list.append([x+'<w-w>'+y for x,y in zip(pre,after)])
    return doc_quat_list