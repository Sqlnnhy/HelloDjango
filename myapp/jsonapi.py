# -*- coding:utf-8 -*-

import json
"""
{
        "button":
        [
            {
                "type": "view",
                "name": "主菜单",
                "url": "http://wxabc.tmqyt.com/admin/",
                "sub_button": [{
                        "type": "view",
                        "name": "子菜单1",
                        "url": "http://www.baidu.com",
                    },
                    {
                        "type": "view",
                        "name": "子菜单2",
                        "url": "http://www.baidu.com",
                    }]
            },
            {
                "type": "view",
                "name": "主菜单",
                "url": "http://wxabc.tmqyt.com/admin/",
                "sub_button": [{
                        "type": "view",
                        "name": "子菜单1",
                        "url": "http://www.baidu.com",
                    },
                    {
                        "type": "view",
                        "name": "子菜单2",
                        "url": "http://www.baidu.com",
                    }]
            }
        ]
    }
"""
# {
#     "type": "view",
#     "name": "主菜单",
#     "url": "http://wxabc.tmqyt.com/admin/",
#     "sub_button": []
# }


class menu_dict(object):
    def __init__(self, types, name, url, sub_button=None):
        if sub_button is None:
            sub_button = []
        self.dict = {"type": types,
                     "name": name,
                     "url": url,
                     "sub_button": sub_button
                     }

    def sub_menu(self, sub):
        if len(self.dict["sub_button"]) <= 4 and isinstance(sub, dict):
            self.dict["sub_button"].append(sub)
        else:
            pass

    def get_dict(self):
        return self.dict


if __name__ == '__main__':
    sub_menu = menu_dict('view', 'names', 'url')
    menu = menu_dict('view', 'name', 'www.baidu.com')
    menu.sub_menu(sub_menu.dict)
    print menu.get_dict()
    print json.dumps(menu.dict)
