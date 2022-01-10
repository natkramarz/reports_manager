def fill_out(driver, login_page_url, login, password):
    driver.get(login_page_url)
    l = driver.find_element_by_name("j_username")
    l.send_keys(login)
    p = driver.find_element_by_name("j_password")
    p.send_keys(password)
    # clicking log in button
    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div/div[4]/div[2]/input").click()