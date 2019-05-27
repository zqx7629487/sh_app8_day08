import allure
import pytest


class TestOne:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试打印123456")
    def test_01(self):
        allure.attach("测试打印成功", "成功123456")
        with open("./as.jpg", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.JPG)

        print(123456)
        assert True
