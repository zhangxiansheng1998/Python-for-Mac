import configparser


def get_ini_value(section, key, file_path='../config.ini'):
    """
    从INI文件中获取指定section和key的值

    Args:
        section (str): 部分名称
        key (str): 键名
        file_path (str, optional): INI文件路径，默认为'config.ini'

    Returns:
        str: 键对应的值，如果未找到键或部分，则返回None
    """
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        value = config.get(section, key)
        return value
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"INI文件读取错误: {e}")
        return None
