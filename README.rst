.. These are the Travis-CI and Coveralls badges for your repository. Replace
   your *github_repository* and uncomment these lines by removing the leading
   two dots.

.. .. image:: https://travis-ci.org/*github_repository*.svg?branch=master
    :target: https://travis-ci.org/*github_repository*

.. .. image:: https://coveralls.io/repos/github/*github_repository*/badge.svg?branch=master
    :target: https://coveralls.io/github/*github_repository*?branch=master


The quick lambda compiler takes quick lambda objects from sidekick and compiles
them either to Python, C or Javascript code. The goal is to improve 
interoperability between Python and other languages that can be useful in some 
common Python applications.


C compiler
==========

The main goal of the C compiler is to help with scientific Python where simple 
and small functions can be defined both in Python and C. The goal is to 
prototype a function in a scientific computation in Python and then later 
convert it to C and have huge speed gains with very little effort.

The main use case is interoperability with Numpy, but it can be used as a simple
code generator for other C applications.

>>> from sidekick import _
>>> from qlcompiler import c_compiler
>>> print(c_compiler.compile(_ + 2))
void function(double _) {
    return _ + 2;
}


Javascript compiler
===================

Similarly to C compiler, the Javascript compiler converts quick lambdas to
Javascript code. It may be useful in web application in order to share code
between the client and the server.

>>> from qlcompiler import js_compiler
>>> print(js_compiler.compile(_ + 2))
function(_) {
    return _ + 2;
}
