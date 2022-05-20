# 系统开发问题记录



### 2021年12月13日

### ISSUES

- 在查询数据时，注意查询到的数据可能会有null，在对查询的数据进行进一步操作时必须确认不是`null`

  ```java
  //com.orchard.assess_sys.service.impl.MenuServiceImpl
  
  public List<Resource> findResource(Integer id) {
      List<Resource> res = new ArrayList<>();
  
      UserInfo user = userInfoMapper.getRolesById(id);
  
      List<Role> roles = user.getRoles();
  
      List<List<Resource>> resources  = new ArrayList<>();
  	
      //erro
      for (Role role : roles) {
          Integer roleId = role.getRoleId();
          //通过Id 获取去资源，如果对应的id没有资源的话，那么得到的是null
          Role role1 = roleMapper.findResourceByRoleId(roleId);
        	//上一步得到的值是null,以下操作会有空指针异常
          List<Resource> resources1 = role1.getResources();
          resources.add(resources1);
      }
  
      //TODO: 去除重复的
      for (List<Resource> list : resources){
          res.addAll(list);
      }
  ```

  









### 2021年12月12日

#### TODO

- [ ] user_info 表中的user_id是表示用户的id，用 `int` 型可能不合适，使用 `string` 或是更大的整数

#### ISSUES

- mybatisPlus的版本`3.4.3.1-->3.4.3.4` ,低版本的会出错。 [参考](https://blog.csdn.net/qq_39114355/article/details/84107895)





---



#### `Integer` `Boolean` 的转换

数据库字段类型是 `bit`, 实体类对应属性为 `Boolean`

前端请求对应的属性的值为 `1` 或 `0`. 将前端的请求中的数据插入数据库























