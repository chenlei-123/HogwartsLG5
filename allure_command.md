pytest -sv test_cal.py --alluredir=./result/
allure generate ./result/ -c -o ./result/report/ --clean
