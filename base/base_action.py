from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, feature, timeout=10, poll=1):
        """
        根据特征，找元素
        :param feature:特征
        :param timeout:超时时间
        :param poll:频率
        :return:元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def base_find_elements(self, feature, timeout=10, poll=1):
        """
        根据特征，找多个符合条件的元素
        :param feature:特征
        :param timeout:超时时间
        :param poll:频率
        :return:元素
        """
        feature_by, feature_value = feature
        elements = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return elements

    def base_click(self, feature):
        self.base_find_element(feature).click()

    def base_input(self, feature, value):
        self.base_find_element(feature).send_keys(value)

    def base_clear(self, feature):
        self.base_find_element(feature).clear()

    def base_press_back(self):
        self.driver.press_keycode(4)

    def base_press_enter(self):
        self.driver.press_keycode(66)