

# Swagger

参考 ： [swagger教程、Swagger视频教程_qq122516902的博客-CSDN博客_swagger教程](https://blog.csdn.net/qq122516902/article/details/89417964)

视频： [swagger api文档、前后端分离工具使用详解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1s4411879K?p=4&spm_id_from=pageDriver)

## 1. SpringBoot 搭建Swagger



### 1.1 导包

Maven依赖如下，版本自选（现在是2.9.2版本）

```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>

```

> http://localhost:8080/swagger-ui  



```xml
 <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-boot-starter</artifactId>
            <version>3.0.0</version>
  </dependency>
```

> http://localhost:8080/swagger-ui/index.html

## 2. 在项目中配置

### 2.1 新建一个类作为配置类

```java
@Component
// 开启Swagger2的自动配置
@EnableSwagger2
public class SwaggerConfig {
    
}

```



> 使用`@EnableSwagger2` 注解开启



### 2.2 配置Swagger实例



```java
@Component
// 开启Swagger2的自动配置
@EnableSwagger2
public class SwaggerConfig {

    // 配置docket以配置Swagger具体参数
    @Bean
    public Docket docket() {
        return new Docket(DocumentationType.SWAGGER_2);
    }

}

```





### 2.3 配置API文档的信息

通过`apiInfo()`属性配置文档信息：

```java
@Component
// 开启Swagger2的自动配置
@EnableSwagger2
public class SwaggerConfig {

    // 配置docket以配置Swagger具体参数
    @Bean
    public Docket docket() {
        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo());
    }


    private ApiInfo apiInfo() {
        Contact contact = new Contact("联系人名字", "http://xxx.xxx.com/联系人访问链接", "联系人邮箱");
        // public ApiInfo(String title, String description, String version, String termsOfServiceUrl, Contact contact, String ", String licenseUrl, Collection<VendorExtension> vendorExtensions) {
        return new ApiInfo("Swagger学习", // 标题
                "学习演示如何配置Swagger", // 描述
                "v1.0", // 版本
                "http://terms.service.url/组织链接", // 组织链接
                contact, // 联系人信息
                "Apach 2.0 许可", // 许可
                "许可链接", // 许可连接
                new ArrayList<>()); // 扩展
    }

}

```



配置后重启访问可以看到如下：

![在这里插入图片描述](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20190420150506547.png)





### 2.4 配置要扫描的接口

构建Docket时通过`select()`方法配置怎么扫描接口。

```java
@Component
// 开启Swagger2的自动配置
@EnableSwagger2
public class SwaggerConfig {

    // 配置docket以配置Swagger具体参数
    @Bean
    public Docket docket() {
        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
                // 通过.select()方法，去配置扫描接口
                .select()
                // RequestHandlerSelectors配置如何扫描接口
                .apis(RequestHandlerSelectors.basePackage("com.example.swaggerexample.controller")).build();
    }


    private ApiInfo apiInfo() {
        Contact contact = new Contact("联系人名字", "http://xxx.xxx.com/联系人访问链接", "联系人邮箱");
        // public ApiInfo(String title, String description, String version, String termsOfServiceUrl, Contact contact, String ", String licenseUrl, Collection<VendorExtension> vendorExtensions) {
        return new ApiInfo("Swagger学习", // 标题
                "学习演示如何配置Swagger", // 描述
                "v1.0", // 版本
                "http://terms.service.url/组织链接", // 组织链接
                contact, // 联系人信息
                "Apach 2.0 许可", // 许可
                "许可链接", // 许可连接
                new ArrayList<>()); // 扩展
    }

}

```



![在这里插入图片描述](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20190420150522272.png)



除了通过包路径配置扫描接口外，还可以通过配置其他方式扫描接口，这里注释一下所有的配置方式：

```java
any() // 扫描所有，项目中的所有接口都会被扫描到
none() // 不扫描接口
withMethodAnnotation(final Class<? extends Annotation> annotation)// 通过方法上的注解扫描，如withMethodAnnotation(GetMapping.class)只扫描get请求
withClassAnnotation(final Class<? extends Annotation> annotation) // 通过类上的注解扫描，如.withClassAnnotation(Controller.class)只扫描有controller注解的类中的接口
basePackage(final String basePackage) // 根据包路径扫描接口

```





### 2.5 配置接口扫描过滤

上述方式可以通过具体的类、方法等扫描接口，还可以配置如何通过请求路径配置：

```java
eturn new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.swaggerexample.controller"))
                // 配置如何通过 path过滤 即这里只扫描 请求以 /user开头的接口
    		   .paths(PathSelectors.ant("/user/**"))
                .build();

```



### 2.6 配置要忽略的请求参数

可以通过`ignoredParameterTypes()`方法去配置要忽略的参数：

```java
// 配置docket以配置Swagger具体参数
    @Bean
    public Docket docket() {
        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
            // 配置要忽略的参数
                .ignoredParameterTypes(HttpServletRequest.class) 
                .select()
       .apis(RequestHandlerSelectors.basePackage("com.example.swaggerexample.controller")).build();
    }


```





### 2.7 配置是否启动 Swagger

通过`enable()`方法配置是否启用swagger，如果是false，swagger将不能在浏览器中访问了：

```java
@Bean
    public Docket docket() {
        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
                .ignoredParameterTypes(HttpServletRequest.class)
                .enable(false) // 配置是否启用Swagger，如果是false，在浏览器将无法访问
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.swaggerexample.controller")).build();
    }

```



如何动态配置当项目处于test、dev环境时显示swagger，处于prod时不显示？

```java
@Bean
    public Docket docket(Environment environment) {
        // 设置要显示swagger的环境
        Profiles of = Profiles.of("dev", "test");
        // 判断当前是处于该环境，通过 enable() 接收此参数判断是否要显示
        boolean b = environment.acceptsProfiles(of);

        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
                .ignoredParameterTypes(HttpServletRequest.class)
                .enable(b) // 配置是否启用Swagger，如果是false，在浏览器将无法访问
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.swaggerexample.controller")).build();
    }

```





### 2.8 配置API分组

如果没有配置分组，默认是default。通过`groupName()`方法即可配置分组：

```java
 @Bean
public Docket docket(Environment environment) {
    return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
        .groupName("user") // 配置分组
        // 省略配置....
}

```



如下图所示，我们配置了`groupName("user")`那么当前接口分组信息为user。

![在这里插入图片描述](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20190420150538822.png)



如何配置多个分组？

配置多个分组只需要配置多个`docket`即可：

```java
@Bean
public Docket docket1() {
    return new Docket(DocumentationType.SWAGGER_2).groupName("group1");
}
@Bean
public Docket docket2() {
    return new Docket(DocumentationType.SWAGGER_2).groupName("group2");
}
@Bean
public Docket docket3() {
    return new Docket(DocumentationType.SWAGGER_2).groupName("group3");
}

```





### 2.9 实体配置

比如当前项目中有这么一个实体

```java
@ApiModel("用户实体")
public class User {
    @ApiModelProperty("用户名")
    private String username;
    @ApiModelProperty("密码")
    private String password;
	// 省略getter/setter
}


```



只要这个实体在**请求接口**的返回值上（即使是泛型），都能映射到实体项中：

![在这里插入图片描述](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20190420151728948.png)



> 注：并不是因为`@ApiModel`这个注解让实体显示在这里了，而是只要出现在接口方法的返回值上的实体都会显示在这里，而`@ApiModel`和`@ApiModelProperty`这两个注解只是为实体添加注释的。
>
> `@ApiModel`为类添加注释
>
> `@ApiModelProperty`为类属性添加注释