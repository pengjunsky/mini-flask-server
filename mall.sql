/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : mall

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-10-30 21:59:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `banner`
-- ----------------------------
DROP TABLE IF EXISTS `banner`;
CREATE TABLE `banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL COMMENT 'Banner名称，通常作为标识',
  `description` varchar(255) DEFAULT NULL COMMENT 'Banner描述',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='banner管理表';

-- ----------------------------
-- Records of banner
-- ----------------------------
INSERT INTO `banner` VALUES ('1', '首页置顶', '首页轮播图', null, '1528938338');

-- ----------------------------
-- Table structure for `banner_item`
-- ----------------------------
DROP TABLE IF EXISTS `banner_item`;
CREATE TABLE `banner_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_id` int(11) NOT NULL COMMENT '外键，关联image表',
  `key_word` varchar(100) NOT NULL COMMENT '执行关键字，根据不同的type含义不同',
  `type` tinyint(4) NOT NULL DEFAULT '1' COMMENT '跳转类型，可能导向商品，可能导向专题，可能导向其他。0，无导向；1：导向商品;2:导向专题',
  `banner_id` int(11) NOT NULL COMMENT '外键，关联banner表',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COMMENT='banner子项表';

-- ----------------------------
-- Records of banner_item
-- ----------------------------
INSERT INTO `banner_item` VALUES ('1', '65', '6', '1', '1', null, '1528938338');
INSERT INTO `banner_item` VALUES ('2', '2', '25', '1', '1', null, '1528938338');
INSERT INTO `banner_item` VALUES ('3', '3', '11', '1', '1', null, '1528938338');
INSERT INTO `banner_item` VALUES ('5', '1', '10', '1', '1', null, '1528938338');

-- ----------------------------
-- Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL COMMENT '分类名称',
  `topic_img_id` int(11) DEFAULT NULL COMMENT '外键，关联image表',
  `description` varchar(100) DEFAULT NULL COMMENT '描述',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COMMENT='商品类目';

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('2', '果味', '6', null, null, null);
INSERT INTO `category` VALUES ('3', '蔬菜', '5', null, null, null);
INSERT INTO `category` VALUES ('4', '炒货', '7', null, null, null);
INSERT INTO `category` VALUES ('5', '点心', '4', null, null, null);
INSERT INTO `category` VALUES ('6', '粗茶', '8', null, null, null);
INSERT INTO `category` VALUES ('7', '淡饭', '9', null, null, null);

-- ----------------------------
-- Table structure for `image`
-- ----------------------------
DROP TABLE IF EXISTS `image`;
CREATE TABLE `image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL COMMENT '图片路径',
  `from` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1 来自本地，2 来自公网',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COMMENT='图片总表';

-- ----------------------------
-- Records of image
-- ----------------------------
INSERT INTO `image` VALUES ('1', '/banner-1a.png', '1', null, null);
INSERT INTO `image` VALUES ('2', '/banner-2a.png', '1', null, null);
INSERT INTO `image` VALUES ('3', '/banner-3a.png', '1', null, null);
INSERT INTO `image` VALUES ('4', '/category-cake.png', '1', null, null);
INSERT INTO `image` VALUES ('5', '/category-vg.png', '1', null, null);
INSERT INTO `image` VALUES ('6', '/category-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('7', '/category-fry-a.png', '1', null, null);
INSERT INTO `image` VALUES ('8', '/category-tea.png', '1', null, null);
INSERT INTO `image` VALUES ('9', '/category-rice.png', '1', null, null);
INSERT INTO `image` VALUES ('10', '/product-dryfruit@1.png', '1', null, null);
INSERT INTO `image` VALUES ('13', '/product-vg@1.png', '1', null, null);
INSERT INTO `image` VALUES ('14', '/product-rice@6.png', '1', null, null);
INSERT INTO `image` VALUES ('16', '/1@theme.png', '1', null, null);
INSERT INTO `image` VALUES ('17', '/2@theme.png', '1', null, null);
INSERT INTO `image` VALUES ('18', '/3@theme.png', '1', null, null);
INSERT INTO `image` VALUES ('19', '/detail-1@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('20', '/detail-2@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('21', '/detail-3@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('22', '/detail-4@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('23', '/detail-5@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('24', '/detail-6@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('25', '/detail-7@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('26', '/detail-8@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('27', '/detail-9@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('28', '/detail-11@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('29', '/detail-10@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('31', '/product-rice@1.png', '1', null, null);
INSERT INTO `image` VALUES ('32', '/product-tea@1.png', '1', null, null);
INSERT INTO `image` VALUES ('33', '/product-dryfruit@2.png', '1', null, null);
INSERT INTO `image` VALUES ('36', '/product-dryfruit@3.png', '1', null, null);
INSERT INTO `image` VALUES ('37', '/product-dryfruit@4.png', '1', null, null);
INSERT INTO `image` VALUES ('38', '/product-dryfruit@5.png', '1', null, null);
INSERT INTO `image` VALUES ('39', '/product-dryfruit-a@6.png', '1', null, null);
INSERT INTO `image` VALUES ('40', '/product-dryfruit@7.png', '1', null, null);
INSERT INTO `image` VALUES ('41', '/product-rice@2.png', '1', null, null);
INSERT INTO `image` VALUES ('42', '/product-rice@3.png', '1', null, null);
INSERT INTO `image` VALUES ('43', '/product-rice@4.png', '1', null, null);
INSERT INTO `image` VALUES ('44', '/product-fry@1.png', '1', null, null);
INSERT INTO `image` VALUES ('45', '/product-fry@2.png', '1', null, null);
INSERT INTO `image` VALUES ('46', '/product-fry@3.png', '1', null, null);
INSERT INTO `image` VALUES ('47', '/product-tea@2.png', '1', null, null);
INSERT INTO `image` VALUES ('48', '/product-tea@3.png', '1', null, null);
INSERT INTO `image` VALUES ('49', '/1@theme-head.png', '1', null, null);
INSERT INTO `image` VALUES ('50', '/2@theme-head.png', '1', null, null);
INSERT INTO `image` VALUES ('51', '/3@theme-head.png', '1', null, null);
INSERT INTO `image` VALUES ('52', '/product-cake@1.png', '1', null, null);
INSERT INTO `image` VALUES ('53', '/product-cake@2.png', '1', null, null);
INSERT INTO `image` VALUES ('54', '/product-cake-a@3.png', '1', null, null);
INSERT INTO `image` VALUES ('55', '/product-cake-a@4.png', '1', null, null);
INSERT INTO `image` VALUES ('56', '/product-dryfruit@8.png', '1', null, null);
INSERT INTO `image` VALUES ('57', '/product-fry@4.png', '1', null, null);
INSERT INTO `image` VALUES ('58', '/product-fry@5.png', '1', null, null);
INSERT INTO `image` VALUES ('59', '/product-rice@5.png', '1', null, null);
INSERT INTO `image` VALUES ('60', '/product-rice@7.png', '1', null, null);
INSERT INTO `image` VALUES ('62', '/detail-12@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('63', '/detail-13@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('65', '/banner-4a.png', '1', null, null);
INSERT INTO `image` VALUES ('66', '/product-vg@4.png', '1', null, null);
INSERT INTO `image` VALUES ('67', '/product-vg@5.png', '1', null, null);
INSERT INTO `image` VALUES ('68', '/product-vg@2.png', '1', null, null);
INSERT INTO `image` VALUES ('69', '/product-vg@3.png', '1', null, null);

-- ----------------------------
-- Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL COMMENT '商品名称',
  `price` decimal(6,2) NOT NULL COMMENT '价格,单位：分',
  `sale` int(11) NOT NULL DEFAULT '0' COMMENT '销量',
  `stock` int(11) NOT NULL DEFAULT '0' COMMENT '库存量',
  `category_id` int(11) DEFAULT NULL,
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL,
  `summary` varchar(50) DEFAULT NULL COMMENT '摘要',
  `main_img_id` int(11) DEFAULT NULL COMMENT '图片外键',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES ('1', '芹菜 半斤', '0.01', '0', '998', '3', '1528938338', null, null, '13');
INSERT INTO `product` VALUES ('2', '梨花带雨 3个', '0.01', '0', '984', '2', '1528938339', null, null, '10');
INSERT INTO `product` VALUES ('3', '素米 327克', '0.01', '0', '996', '7', '1528938340', null, null, '31');
INSERT INTO `product` VALUES ('4', '红袖枸杞 6克*3袋', '0.01', '0', '998', '6', '1528938341', null, null, '32');
INSERT INTO `product` VALUES ('5', '春生龙眼 500克', '0.01', '0', '995', '2', '1528938342', null, null, '33');
INSERT INTO `product` VALUES ('6', '小红的猪耳朵 120克', '0.01', '0', '997', '5', '1528938343', null, null, '53');
INSERT INTO `product` VALUES ('7', '泥蒿 半斤', '0.01', '0', '998', '3', '1528938344', null, null, '68');
INSERT INTO `product` VALUES ('8', '夏日芒果 3个', '0.01', '0', '995', '2', '1528938345', null, null, '36');
INSERT INTO `product` VALUES ('9', '冬木红枣 500克', '0.01', '0', '996', '2', '1528938346', null, null, '37');
INSERT INTO `product` VALUES ('10', '万紫千凤梨 300克', '0.01', '0', '996', '2', '1528938347', null, null, '38');
INSERT INTO `product` VALUES ('11', '贵妃笑 100克', '0.01', '0', '994', '2', '1528938369', null, null, '39');
INSERT INTO `product` VALUES ('12', '珍奇异果 3个', '0.01', '0', '999', '2', '1528938349', null, null, '40');
INSERT INTO `product` VALUES ('13', '绿豆 125克', '0.01', '0', '999', '7', '1528938350', null, null, '41');
INSERT INTO `product` VALUES ('14', '芝麻 50克', '0.01', '0', '999', '7', '1528938351', null, null, '42');
INSERT INTO `product` VALUES ('15', '猴头菇 370克', '0.01', '0', '999', '7', '1528938352', null, null, '43');
INSERT INTO `product` VALUES ('16', '西红柿 1斤', '0.01', '0', '999', '3', '1528938353', null, null, '69');
INSERT INTO `product` VALUES ('17', '油炸花生 300克', '0.01', '0', '999', '4', '1528938354', null, null, '44');
INSERT INTO `product` VALUES ('18', '春泥西瓜子 128克', '0.01', '0', '997', '4', '1528938355', null, null, '45');
INSERT INTO `product` VALUES ('19', '碧水葵花籽 128克', '0.01', '0', '999', '4', '1528938356', null, null, '46');
INSERT INTO `product` VALUES ('20', '碧螺春 12克*3袋', '0.01', '0', '999', '6', '1528938357', null, null, '47');
INSERT INTO `product` VALUES ('21', '西湖龙井 8克*3袋', '0.01', '0', '998', '6', '1528938358', null, null, '48');
INSERT INTO `product` VALUES ('22', '梅兰清花糕 1个', '0.01', '0', '997', '5', '1528938359', null, null, '54');
INSERT INTO `product` VALUES ('23', '清凉薄荷糕 1个', '0.01', '0', '998', '5', '1528938360', null, null, '55');
INSERT INTO `product` VALUES ('25', '小明的妙脆角 120克', '0.01', '0', '999', '5', '1528938361', null, null, '52');
INSERT INTO `product` VALUES ('26', '红衣青瓜 混搭160克', '0.01', '0', '999', '2', '1528938362', null, null, '56');
INSERT INTO `product` VALUES ('27', '锈色瓜子 100克', '0.01', '0', '998', '4', '1528938363', null, null, '57');
INSERT INTO `product` VALUES ('28', '春泥花生 200克', '0.01', '0', '999', '4', '1528938364', null, null, '58');
INSERT INTO `product` VALUES ('29', '冰心鸡蛋 2个', '0.01', '0', '999', '7', '1528938365', null, null, '59');
INSERT INTO `product` VALUES ('30', '八宝莲子 200克', '0.01', '0', '999', '7', '1528938366', null, null, '14');
INSERT INTO `product` VALUES ('31', '深涧木耳 78克', '0.01', '0', '999', '7', '1528938367', null, null, '60');
INSERT INTO `product` VALUES ('32', '土豆 半斤', '0.01', '0', '999', '3', '1528938368', null, null, '66');
INSERT INTO `product` VALUES ('33', '青椒 半斤', '0.01', '0', '999', '3', '1528938369', null, null, '67');

-- ----------------------------
-- Table structure for `product_image`
-- ----------------------------
DROP TABLE IF EXISTS `product_image`;
CREATE TABLE `product_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_id` int(11) NOT NULL COMMENT '外键，关联图片表',
  `order` int(11) NOT NULL DEFAULT '0' COMMENT '图片排序序号',
  `product_id` int(11) NOT NULL COMMENT '商品id，外键',
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product_image
-- ----------------------------
INSERT INTO `product_image` VALUES ('4', '19', '1', '11', null, null);
INSERT INTO `product_image` VALUES ('5', '20', '2', '11', null, null);
INSERT INTO `product_image` VALUES ('6', '21', '3', '11', null, null);
INSERT INTO `product_image` VALUES ('7', '22', '4', '11', null, null);
INSERT INTO `product_image` VALUES ('8', '23', '5', '11', null, null);
INSERT INTO `product_image` VALUES ('9', '24', '6', '11', null, null);
INSERT INTO `product_image` VALUES ('10', '25', '7', '11', null, null);
INSERT INTO `product_image` VALUES ('11', '26', '8', '11', null, null);
INSERT INTO `product_image` VALUES ('12', '27', '9', '11', null, null);
INSERT INTO `product_image` VALUES ('13', '28', '11', '11', null, null);
INSERT INTO `product_image` VALUES ('14', '29', '10', '11', null, null);
INSERT INTO `product_image` VALUES ('18', '62', '12', '11', null, null);
INSERT INTO `product_image` VALUES ('19', '63', '13', '11', null, null);

-- ----------------------------
-- Table structure for `product_property`
-- ----------------------------
DROP TABLE IF EXISTS `product_property`;
CREATE TABLE `product_property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT '' COMMENT '详情属性名称',
  `detail` varchar(255) NOT NULL COMMENT '详情属性',
  `product_id` int(11) NOT NULL COMMENT '商品id，外键',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product_property
-- ----------------------------
INSERT INTO `product_property` VALUES ('1', '品名', '杨梅', '11', null, null);
INSERT INTO `product_property` VALUES ('2', '口味', '青梅味 雪梨味 黄桃味 菠萝味', '11', null, null);
INSERT INTO `product_property` VALUES ('3', '产地', '火星', '11', null, null);
INSERT INTO `product_property` VALUES ('4', '保质期', '180天', '11', null, null);
INSERT INTO `product_property` VALUES ('5', '品名', '梨子', '2', null, null);
INSERT INTO `product_property` VALUES ('6', '产地', '金星', '2', null, null);
INSERT INTO `product_property` VALUES ('7', '净含量', '100g', '2', null, null);
INSERT INTO `product_property` VALUES ('8', '保质期', '10天', '2', null, null);

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` varchar(50) DEFAULT NULL,
  `email` varchar(24) DEFAULT NULL,
  `nickname` varchar(24) DEFAULT NULL,
  `userPic` varchar(255) DEFAULT NULL,
  `auth` smallint(6) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `openid` (`openid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1539848235', '1540623233', '1', 'oapee4lTOfFg1hpx0lQ5x_HcURUM', null, '小毛', '14612.b0.upaiyun.com/2017/12/19/cbe1427840f5c6b4801abcdd8b6a4e18.jpg', '1', null);
INSERT INTO `user` VALUES ('1539848235', null, '2', null, 'wwe1221@qq.com', 'nihaoe1212', null, '1', 'pbkdf2:sha256:50000$r070DVfB$bbd0d1995a7381c7d5c33cbe8aaa683653b44b3464cea77f4330138095530fce');
INSERT INTO `user` VALUES ('1540349983', null, '4', null, 'wwe12221@qq.com', 'nihaoe12212', null, '1', 'pbkdf2:sha256:50000$8FLGWA6K$f71dc8cae1ad00cc9ba7bca571400ab40835be02837cf3eb5db9bc9d4f87550b');
INSERT INTO `user` VALUES ('1540363560', null, '5', null, 'wwe122221@qq.com', 'nihaoe12212', null, '1', 'pbkdf2:sha256:50000$FjAW1u03$cf508e1ff3b562aec3c2eeea6a0bdde4eb678ddd79dba7ae26fbaab49bfd447f');
INSERT INTO `user` VALUES ('1540622646', null, '6', null, 'wwe1222221@qq.com', 'nihaoe122122', null, '1', 'pbkdf2:sha256:50000$8ibOAwHs$c573ce052f20036efe1af7afb61dd99a03fe45310505afe17b87bc10682af151');
