from antachawy.definitions import LexemasAntachawy, EtiquetasAntachawy, primeros
from antachawy.scanner import Scanner

from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

def render_tree(root: object):
    for pre,fill,node in RenderTree(root):
        print("%s%s" % (pre, node.name))

