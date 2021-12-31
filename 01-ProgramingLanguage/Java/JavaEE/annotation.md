# 注解说明



## 1. Spring



| 注解            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| @Component      | 使用在类上用于实例化Bean                                     |
| @Controller     | 使用在web层类上用于实例化Bean                                |
| @Service        | 使用在service层类上用于实例化Bean                            |
| @Repository     | 使用在dao层类上用于实例化Bean                                |
| @Autowired      | 使用在字段上用于根据类型依赖注入                             |
| @Qualifier      | 结合@Autowired一起使用用于根据名称进行依赖注入               |
| @Resource       | 相当于@Autowired+@Qualifier，按照名称进行注入                |
| @Value          | 注入普通属性                                                 |
| @Scope          | 标注Bean的作用范围                                           |
| @PostConstruct  | 使用在方法上标注该方法是Bean的初始化方法                     |
| @PreDestroy     | 使用在方法上标注该方法是Bean的销毁方法                       |
| @Configuration  | 用于指定当前类是一个Spring 配置类，当创建容器时会从该类上加载注解 |
| @ComponentScan  | 用于指定Spring 在初始化容器时要扫描的包。作用和在Spring 的xml 配置文件中的<context:component-scan base-package="com.itheima"/>一样 |
| @Bean           | 使用在方法上，标注将该方法的返回值存储到Spring 容器中        |
| @PropertySource | 用于加载.properties 文件中的配置                             |
| @Import         | 用于导入其他配置类                                           |











## 2. SpringMVC

### @RequestMapping

`@RequestMapping`
作用：用于建立请求URL 和处理请求方法之间的对应关系
位置：

- 类上，请求URL 的第一级访问目录。此处不写的话，就相当于应用的根目录
- 方法上，请求URL 的第二级访问目录，与类上的使用@ReqquestMapping标注的一级目录一起组成访问虚拟路径

属性：

- `value`：用于指定请求的URL。它和path属性的作用是一样的
- `method`：用于指定请求的方式
- `params`：用于指定限制请求参数的条件。它支持简单的表达式。要求请求参数的key和value必须和配置的一模一样

例如：

- `params= {"accountName"}`，表示请求参数必须有accountName
- `params= {"moeny!100"}`，表示请求参数中money不能是100



### @ResponseBody

`@ResponseBody`注解告知SpringMVC框架方法返回的数据放到响应体中，而不是直接返回到页面

```java
@RequestMapping("/quick5")
@ResponseBody
public String quickMethod5() throws IOException {
    return "hello springMVC!!!";
}
```



> 在方法上添加@ResponseBody就可以返回json格式的字符串，但是这样配置比较麻烦，配置的代码比较多，因此，我们可以使用mvc的注解驱动代替上述配置。

```xml
<!--mvc的注解驱动-->
<mvc:annotation-driven/>
```



### 参数绑定注解@requestParam

注解`@RequestParam`有如下参数可以使用：

- `value`：与请求参数名称
- `required`：此在指定的请求参数是否必须包括，默认是true，提交时如果没有此参数则报错
- `defaultValue`：当没有指定请求参数时，则使用指定的默认值赋值

```java
@RequestMapping("/quick14")
@ResponseBody
public void quickMethod14(@RequestParam(value="name",required = false,defaultValue = "itcast") String username) throws IOException {
    System.out.println(username);
}
```



### 获得Restful风格的参数

Restful风格的请求是使用“url+请求方式”表示一次请求目的的，HTTP 协议里面四个表示操作方式的动词如下：-   

- `GET`：用于获取资源
- `POST`：用于新建资源
- `PUT`：用于更新资源
- `DELETE`：用于删除资源

例如：

- `/user/1` 	  GET ：得到id = 1 的user
- `/user/1`      DELETE：删除id = 1 的user
- `/user/1`      PUT：更新id = 1 的user
- `/user`          POST：新增user





### 获得请求头 

#### @RequestHeader

使用@RequestHeader可以获得请求头信息
`@RequestHeader`注解的属性如下：

- `value`：请求头的名称
- `required`：是否必须携带此请求头

```java
@RequestMapping("/quick17")
@ResponseBody
public void quickMethod17(@RequestHeader(value = "User-Agent",required = false) String headerValue){
    System.out.println(headerValue);
}
```





#### @CookieValue

使用@CookieValue可以获得指定Cookie的值
`@CookieValue`注解的属性如下：

- `value`：指定cookie的名称
- `required`：是否必须携带此cookies

```java
@RequestMapping("/quick18")
@ResponseBody
public void quickMethod18(
    @CookieValue(value = "JSESSIONID",required = false) String jsessionid){
    System.out.println(jsessionid);
}
```









## 3. Mybatis

### @Param

对于多个参数的方法在参数前加上 `@Param` 注解

接口中方法定义

```java
User findByCondition(@Param("id") Integer id,@Param("username") String username);
```

mapper

```java
<select id="findByCondition" resultType="com.sangeng.pojo.User">
         select * from user where id = #{id} and username = #{username}
</select>
```













## 4. MybatisPlus





## 5. SpringBoot





## 6. lombok





## 7. Swagger

