#!/bin/bash
ssh manduca@m6 /usr/local/es-dyn/bin/apachectl restart
ssh manduca@m13 /usr/local/es-dyn/bin/apachectl restart
ssh manduca@m17 /usr/local/es-dyn/bin/apachectl restart
