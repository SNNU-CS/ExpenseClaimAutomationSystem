<template>
<div>
    <el-dialog title="密码修改" :visible=true style="width:1000px; margin:0 auto">
  <el-form 
     :rules="rules"
     :model="pwdList"
     style="width:350px;"
     status-icon
     ref="pwdList"
  >
        <el-form-item prop="oldPwd"  label="原密码" label-width='100px'  >
            <el-input v-model="pwdList.oldPwd"  placeholder="请输入原密码" show-password />
        </el-form-item>
  
        <el-form-item  prop="newPwd" label="新密码" label-width='100px' >
            <el-input v-model="pwdList.newPwd"  placeholder="新密码（5-12大小写字母、数字）" show-password />
        </el-form-item>

        <el-form-item prop="newPwd2"  label="确认密码" label-width='100px' >
          <el-input v-model="pwdList.newPwd2"  placeholder="确认密码（5-12大小写字母、数字）" show-password />
        </el-form-item>
  </el-form>
  
    <el-dialog
      width="30%"
      title="修改成功"
      :visible.sync="rebuldDialogVisible"
      append-to-body>
      <span>密码修改成功，下次登录生效！</span>
    <span slot="footer" class="dialog-footer">
      <el-button type="primary" @click="rebuldDialogVisible = false">确定</el-button>
    </span>
    </el-dialog>
    <div slot="footer" class="dialog-footer">
      <el-button @click="resetForm('pwdList')">取 消</el-button>
      <el-button type="primary" @click="innerVisible('pwdList')">确认</el-button>
    </div>
  </el-dialog>
 
  </div>
</template>

<script>
const pwdListDefault = {
  oldPwd: null,
  newPwd: null,
  newPwd2: null
}
  export default {
    methods:{
      resetForm(pwdList) {
        this.$refs[pwdList].resetFields();
      },
      innerVisible(){
        this.rebuldDialogVisible=true
      }
    },
    data() {
    var checkPwd = (rule, value, callback) => {
      if (value !== this.pwdList.newPwd) {
        callback(new Error('密码不一致'))
      } else {
        callback()
      }
    }
      return {
       rebuldDialogVisible: false,
       pwdList: Object.assign({}, pwdListDefault),
        rules: {
        loginName: [
          { required: true, message: '请输入用户登录名', trigger: 'blur' },
          { min: 2, max: 30, message: '长度在 2 到 20 个字符', trigger: 'blur' }
        ],
        authKey: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        oldPwd: [
          { required: true, message: '请输入旧密码', trigger: 'blur' }
        ],
        newPwd: [
          { required: true, message: '请输入新密码', trigger: 'blur' }
        ],
        newPwd2: [
          { required: true, message: '请再次输入新密码', trigger: 'blur' },
          { validator: checkPwd, trigger: 'blur' }
        ]
      },
        outerVisible: false,
      };
    }
  }
</script>
