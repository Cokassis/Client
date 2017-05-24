# >>>>>> 功能测试1
# 功能测试1:用户从主页进入
# >>>>>> 功能测试1.1
# 功能测试1.1：从主页搜索框开始到完成下单支付的整个流程。
# 
# 用户进入主页，看到搜索框，点击搜索框进入搜索页面
# 用户看到页面中的热门搜索一栏有5项热门搜索的内容
# get: customer.views.top_search_dish
# return = {
#     'search_keywords': [
#         {
#             'keyword': '番茄炒蛋'
#         },
#         {
#             'keyword': '酸辣土豆丝'
#         },
#         {
#             'keyword': '土豆烧牛肉'
#         },
#         {
#             'keyword': '黑椒牛肉'
#         },
#         {
#             'keyword': '回锅肉'
#         }
#     ]
# }
# 用户看到智能推荐栏有3项推荐的菜品
# get: customer.views.recommend_dish
# return = {
#     'dishes': [
#         {
#             'name': '番茄炒蛋',
#             'est_price': 11.5,
#             'order_count': 13
#         },
#         {
#             'name': '土豆烧牛肉',
#             'est_price': 11.5,
#             'order_count': 6
#         },
#         {
#             'name': '黑椒牛肉',
#             'est_price': 11.5,
#             'order_count': 8
#         }
#     ]
# }
# >>>>>> 分支1.11
# 分支1.11:输入关键字,搜索关键字
# 用户在搜索框输入"番茄",点击搜索
# 用户发现热门搜索框和智能推荐框消失了
# 用户看到在当前页面出现了搜索结果框
# 用户看到搜索结果框内有按"番茄"搜索出来的若干项结果,其中包含了相关的食材和菜品
# get: food.views.search  ---完成
# send = {
#     'search_str': '番茄'
# }
# return = {
#     'dishes':
#         [
#             {
#                 'id': 1,
#                 'name': '番茄炒蛋',
#                 'estPrice': 6.5,
#                 'discount': 1.5,
#                 'like': 5
#             },
#             {
#                 'id': 1,
#                 'name': '番茄土豆片',
#                 'estPrice': 9,
#                 'discount': 2.5,
#                 'like': 3
#             },
#             {
#                 'id': 1,
#                 'name': '红烧牛肉',
#                 'estPrice': 19,
#                 'discount': 2.5,
#                 'like': 3
#             },
#             {
#                 'id': 1,
#                 'name': '酸辣土豆丝',
#                 'estPrice': 8,
#                 'discount': 1.5,
#                 'like': 4
#             },
#             {
#                 'id': 1,
#                 'name': '糖醋排骨',
#                 'estPrice': 17,
#                 'discount': 2.5,
#                 'like': 5
#             }
#         ],
#     'materials':
#         [
#             {
#                 'id': 1,
#                 'name': '番茄',
#                 'breed': '大红番茄'
#             },
#             {
#                 'id': 1,
#                 'name': '番茄',
#                 'breed': '粉红番茄'
#             }
#         ]
# }
# 
# >>>>>> 分支1.111
# 分支1.111:点击搜索到的菜品
# 用户看到搜索结果中有"番茄炒蛋",用户点击了"番茄炒蛋",用户看到打开了新的"番茄炒蛋"的页面
# 
# 页面的标题为"番茄炒蛋",有两张番茄炒蛋的图片,有估计的价格,有结算优惠价,有自己对"番茄炒饭"的评级,
# 页面上有食材名为"番茄",品种为"大红番茄",食材用量为2个,重量约为0.7千克,属于小个的番茄,番茄的供应商为"连贵-蔬菜档"
# 页面上有食材名为"鸡蛋",品种为"农家蛋",食材用量为4个,重量约为1.2千克,鸡蛋的供应商为"品泰贸易有限公司"
# get: food.views.get_dish_detail  ---完成
# send = {
#     'dish_id': id_of_fan_qie_chao_dan
# }
# return = {
#     'id': resp_json['id'],
#     'name': '番茄炒蛋',
#     'estPrice': 6.5,
#     'discount': 1.5,
#     'like': 5,
#     'materials': [
#         {
#             'id': resp_json['materials'][0]['id'],
#             'name': '番茄',
#             'breed': '大红番茄',
#             'mean_weight': 0.35,
#             'unit': '个',
#             'amount': 2,
#             'size': '中',
#             'supplier': '连贵-蔬菜档'
#         },
#         {
#             'id': resp_json['materials'][1]['id'],
#             'name': '鸡蛋',
#             'breed': '农家蛋',
#             'mean_weight': 0.3,
#             'unit': '个',
#             'amount': 4,
#             'size': '',
#             'supplier': '品泰贸易有限公司'
#         }
#     ]
# }
# 用户发现页面上有一个增加食材按钮
# >>>>>>分支1.1111 用户点击增加食材按钮
# 用户发现页面跳转到search_foods.html
# 用户发现SearchFoods页面中的热门搜索里有几项热搜食材,分别为: 姜, 葱, 蒜. 热搜食材均有可能作为番茄炒蛋的食材
# get: customer.views.top_search_material
# return = {
#     'material_keyword': [
#         {
#             'keyword': '姜'
#         },
#         {
#             'keyword': '葱'
#         },
#         {
#             'keyword': '蒜'
#         }
#     ]
# }
# 用户发现SearchFoods页面的搜索框, 并输入"姜", 点击搜索按钮, 用户发现页面出现了: 沙姜, 子姜, 老姜三种食材.
# get: food.views.search_material  ---完成
# send = {
#     'search_str': '姜'
# }
# return = {
#     'materials': [
#         {
#             'id': *,
#             'name': '沙姜',
#             'unit_price': '',
#             'unit': '元/kg',
#             'supplier': ''
#         },
#         {
#             'id': *,
#             'name': '子姜',
#             'unit_price': '',
#             'unit': '元/kg',
#             'supplier': ''
#         },
#         {
#             'id': *,
#             'name': '老姜',
#             'unit_price': '',
#             'unit': '元/kg',
#             'supplier': ''
#         }
#     ]
# }
# 用户点击老姜, 发现弹出了一个对话框, 对话框提示"是否加入菜品?" 用户点击确定
#
# post: food.views.add_material_to_dish
# send = {
#     'material_id': id_of_lao_jiang,
#     'dish_id': id_of_fan_qie_chao_dan
# }
# return = {
#     'success': True,
#     'str': '番茄炒蛋 食材+1'
# }
# test:
# len(Dish.objects.get(id=id_of_fan_qie_chao_dan).material_set.filter(id=id_of_lao_jiang)) == 1
#
# 用户点击SearchFoods上的返回按钮, 返回番茄炒蛋页面, 发现页面上多了一项食材, 食材的名字为"姜", 别名为"老姜", 设置食材的子页面自动弹出
# get: food.views.get_dish_detail (函数同上)
# send = {
#     'dish_id': id_of_fan_qie_chao_dan
# }
# return = {
#     'id': resp_json['id'],
#     'name': '番茄炒蛋',
#     'estPrice': 6.5,
#     'discount': 1.5,
#     'like': 5,
#     'materials': [
#         {
#             'id': resp_json['materials'][0]['id'],
#             'name': '番茄',
#             'breed': '大红番茄',
#             'mean_weight': 0.35,
#             'unit': '个',
#             'amount': 2,
#             'size': '中',
#             'supplier': '连贵-蔬菜档'
#         },
#         {
#             'id': resp_json['materials'][1]['id'],
#             'name': '鸡蛋',
#             'breed': '农家蛋',
#             'mean_weight': 0.3,
#             'unit': '个',
#             'amount': 4,
#             'size': '',
#             'supplier': '品泰贸易有限公司'
#         },
#         {
#             'id': resp_json['materials'][2]['id'],
#             'name': '姜',
#             'breed': '老姜',
#             'mean_weight': 0.3,
#             'unit': '',
#             'amount': -1,
#             'size': '',
#             'supplier': '品泰贸易有限公司'
#         }
#     ]
# }
#
# get: food.views.get_dish_material_info_opts
# {
#     'weight_intervals': [
#         {
#             'max_weight': 0.2,
#             'min_weight': 0.1,
#             'note': '少量',
#             'unit': 'kg/个'
#         },
#         {
#             'max_weight': 0.3,
#             'min_weight': 0.2,
#             'note': '中等',
#             'unit': 'kg/个'
#         },
#         {
#             'max_weight': 0.5,
#             'min_weight': 0.3,
#             'note': '较多',
#             'unit': 'kg/个'
#         }
#     ]
# }
# 用户选择了中等量的姜, 并输入3份并确定
# post: food.views.modify_dish_edit_material
# send = {
#     'dish_id': 'id_of_dish',
#     'material_info': {
#         'id': 'id_of_material',
#         'weight_int_id': 'id_of_weight_interval',
#         'quantity': 3
#     }
# }
# <<<<<< 分支测试1.1111尾部
# 用户发现页面上有一个加入购物车按钮
# >>>>>>分支1.1112 用户点击加入购物车按钮
# 用户发现当前页面弹出了一句话"番茄炒蛋 +1"
# post: customer.views.add_dish_to_cart
# send = {
#     'dish_id': id_of_fan_qie_chao_dan
#     'user_cart_id': id_of_user_cart
# }
# return = {
#     'success': True,
#     'str': '番茄炒蛋 +1'
# }
# 用户点击页面上的返回按钮, 一直返回到主页, 用户点击购物车
# 用户发现购物车里有一项菜品: 番茄炒蛋
# get: customer.views.get_shopping_cart
# send = {
#     'user_id': id_of_customer
# }
# return = {
#     'est_price': 9,
#     'deposit': 0,
#     'discount': 0.8,
#     'dishes': [
#         {
#             'name': '番茄炒蛋',
#             'est_price': 9,
#             'materials': ['大红番茄', '农家蛋', '老姜']
#         }
#     ]
# }
#
# 用户点击预订按钮, 跳转至支付页面
# get: customer.views.get_order_detail
# send = {
#     'user_id': 'id_of_customer',
#     'dishes': ['ids_of_dishes'],
#     'materials': ['ids_of_materials']
# }
return = {
    'customer': {
        'name': '',
        'address': '',
        'phone': ''
    },
    'dishes': [
        {
            'name': '番茄炒蛋',
            'est_price': 9.0,
            'materials': [
                {
                    'name': '大红番茄',
                    'count': 2,
                    'unit': '个'
                },
                {
                    'name': '鸡蛋',
                    'count': 3,
                    'unit': '个'
                }
            ]
        }
    ],
    'materials': [
        {
            'name': '莲藕',
            'est_price': 3.6,
            'count': '2',
            'unit': '节',
            'weight': 2.5
        }
    ]
}
# <<<<<< 分支测试1.1112尾部
# 用户发现页面上有一个立即购买按钮
# >>>>>>分支1.1111 用户点击增加食材按钮
# 
# <<<<<< 分支测试1.1111尾部
# <<<<<< 分支测试1.111尾部
# <<<<<< 分支测试1.11尾部
# <<<<<< 功能测试1.1尾部
# <<<<<< 功能测试1尾部
