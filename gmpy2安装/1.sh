#! /bin/bash
mkdir -p $HOME/src
mkdir -p $HOME/static
v=1.4.18
cd $HOME/src
wget http://ftp.gnu.org/gnu/m4/m4-${v}.tar.gz
tar xf m4-${v}.tar.gz && cd m4-${v}
./configure -prefix=/usr/local
make && make check && make install
v=6.1.2
cd $HOME/src
tar -jxvf gmp-${v}.tar.bz2 && cd gmp-${v}
./configure --prefix=$HOME/static --enable-static --disable-shared --with-pic
make && make check && make install
v=4.0.2
cd $HOME/src
tar -jxvf mpfr-${v}.tar.bz2 && cd mpfr-${v}
./configure --prefix=$HOME/static --enable-static --disable-shared --with-pic --with-gmp=$HOME/static
make && make check && make install
v=1.1.0
cd $HOME/src
tar -zxvf mpc-${v}.tar.gz && cd mpc-${v}
./configure --prefix=$HOME/static --enable-static --disable-shared --with-pic --with-gmp=$HOME/static --with-mpfr=$HOME/static
make && make check && make install
v=2-2.1.0a1
cd $HOME/src
wget https://github.com/aleaxit/gmpy/releases/download/gmpy${v}/gmpy${v}.tar.gz
tar xf gmpy${v}.tar.gz && cd gmpy${v}
python setup.py build_ext --static=$HOME/static install