@echo off
setlocal
pushd "%~dp0"

python -m pytest --html=report.html --self-contained-html %*
set "TEST_EXIT=%ERRORLEVEL%"

if exist "report.html" (
    start "" "%~dp0report.html"
) else (
    echo No HTML report was generated. Check that pytest and pytest-html are installed.
)

popd
exit /b %TEST_EXIT%
