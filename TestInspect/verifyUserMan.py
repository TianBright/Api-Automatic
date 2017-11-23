#coding= utf-8
import sys
import unittest

sys.path.append("..")

from apiconfig import *
from User.proUserMan import *
from User.userbody import *


class TestUserManage(unittest.TestCase):
    def setUp(self):
        self.TUM = UserManage(headers,userToken,cteUserBody,cteMultiUsrBody,setPWordBody,nicknameBody)
    def testClitSecret_1(self):
        u'验证获取client secret'
        global client_id,client_secret
        result,client_id,client_secret = self.TUM.getClitSecret()
        self.assertTrue(result,True)
    def testGetAdmToken_2(self):
        u'验证获取admin的Token'
        self.assertEqual(self.TUM.getAdminToken(client_id,client_secret),200)
    def testUserToken_3(self):
        u'验证获取用户的Token'
        self.assertEqual(self.TUM.getUserToken(),200)
    def testGetAllUser_4(self):
        u'验证获取所有用户'
        self.assertEqual(self.TUM.getAllUser(),200)
    def testCrteUser_5(self):
        u'验证创建用户'
        self.assertEqual(self.TUM.CreateUser(),200)
    def testCteMulUser_6(self):
        u'验证创建多个用户'
        self.assertEqual(self.TUM.CrteMulieUser(),200)
    def testGetUsrDetail_7(self):
        u'验证获取用户详情'
        self.assertEqual(self.TUM.getUserDetail(),200)
    def testMulUsrDetail_8(self):
        u'验证获取多个用户详情'
        self.assertEqual(self.TUM.getMulUsrDetail(),200)
    def testChkOnlineStat_9(self):
        u'验证检查用户是否在线'
        self.assertEqual(self.TUM.ChkOnlineStat(),200)
    def testDelUser_10(self):
        u'验证删除一个用户'
        self.assertEqual(self.TUM.deleteUser("rest116"),200)
        self.TUM.deleteUser("rest117")
        self.TUM.deleteUser("rest118")
        self.TUM.deleteUser("rest119")
        self.TUM.deleteUser("rest120")
        self.TUM.deleteUser("rest121")

    def testDelMulUser_11(self):
        u'验证删除多个用户'
        self.assertEqual(self.TUM.delMultiUser(),200)
    def testResetPword_12(self):
        u'验证修改用户密码'
        self.assertEqual(self.TUM.ResetPword(),200)
    def testModNickname_13(self):
        u'验证修改nickname'
        self.assertEqual(self.TUM.ModifyNickname(),200)
    def testAddFriend_14(self):
        u'验证为用户添加一个好友'
        self.assertEqual(self.TUM.addFriends(user1,user2),200)
        self.TUM.addFriends(user1, user3)
        self.TUM.addFriends(user1, user4)
        self.TUM.addFriends(user1, user5)
    def testDelFriend_15(self):
        u'验证删除用户的一个好友'
        self.assertEqual(self.TUM.delFriends(user1, user5),200)
    def testGetFridList_16(self):
        u'验证获取好友列表'
        self.assertEqual(self.TUM.FriendsList(user1),200)
    def testMvToBlack_17(self):
        u'验证将好友移到黑名单'
        self.assertEqual(self.TUM.MvToBlack(user1,user2),200)
    def testGetBlackList_18(self):
        u'验证获取黑名单列表'
        self.assertEqual(self.TUM.GetBlackList(user1),200)
    def testRmBlkList_19(self):
        u'验证将好友从黑名单列表移除'
        self.assertEqual(self.TUM.RmBlkList(user1,user2),200)
    def testDeactivUser_20(self):
        u'验证Deactivate用户'
        self.assertEqual(self.TUM.DeactivateUser(user1),200)
    def testActivUser_21(self):
        u'验证Activate User'
        self.assertEqual(self.TUM.ActivateUser(user1),200)
    def testDsconnectUser_22(self):
        u'验证Disconnect User'
        self.assertEqual(self.TUM.DisconnectUser(),200)



