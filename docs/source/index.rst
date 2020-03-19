Services
=========

**services** 는 **Flacon** 을 사용하는 단순한 플라스크 애플리케이션 입니다.

이 애플리케이션은 :func:`falcon.create_app` 을 통해 생성됩니다.

.. literalinclude:: ../../services/app.py

:func:`create_app` 에 전달되는 :file:`settings.ini` 파일은 플라스크 앱을 실행하는데 필요한 DEBUG 플래그 같은 옵션을 포함합니다.

.. literalinclude:: ../../services/settings.ini