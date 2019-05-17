from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("tables",  ["vablut\modules\\tables.py"]),
    Extension("ashton",  ["vablut\modules\\ashton.py"]),
    Extension("cache",   ["vablut\modules\\cache.py"]),
    Extension("Utils",   ["vablut\modules\\Utils.py"]),
    Extension("base",    ["vablut\evaluate\\base.py"]),
    Extension("evaldiff",           ["vablut\evaluate\\evaldiff.py"]),
    Extension("evaluate_escapist",  ["vablut\evaluate\\evaluate_escapist.py"]),
    Extension("evaluate_gl_esc",    ["vablut\evaluate\\evaluate_gl_esc.py"]),
    Extension("evaluate_glesc_ks",  ["vablut\evaluate\\evaluate_glesc_ks.py"]),
    Extension("evaluate_glutton",   ["vablut\evaluate\\evaluate_glutton.py"]),
    Extension("moveorder",          ["vablut\evaluate\\moveorder.py"]),
    Extension("base",       ["vablut\engine\\base.py"]),
    Extension("alphabeta",  ["vablut\engine\\alphabeta.py"]),
    Extension("cached",     ["vablut\engine\\cached.py"]),
    Extension("greedy",     ["vablut\engine\\greedy.py"]),
    Extension("human",      ["vablut\engine\\human.py"]),
    Extension("negamax",    ["vablut\engine\\negamax.py"]),
    Extension("pvs",        ["vablut\engine\\pvs.py"]),
    Extension("rand",     ["vablut\engine\\rand.py"]),
    Extension("board",     ["vablut\\board.py"]),
    Extension("game",     ["vablut\game.py"]),
    Extension("runny",     ["vablut\\runny.pyx"])
]

setup(
    name = 'test',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)