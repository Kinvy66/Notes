

# D1



## 1. Mybatis环境搭建



### 1.1 使用Maven创建工程

独立的mybatis框架，不集成其他（spring或springboot)

**mavenv坐标导入**

```xml
<dependencies>
    <!--mybatis依赖-->
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
        <version>3.5.4</version>
    </dependency>
    <!--mysql驱动-->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>8.0.25</version>
    </dependency>
    <!--测试-->
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13.2</version>
        <scope>test</scope>
    </dependency>
    <!--日志-->
    <dependency>
        <groupId>log4j</groupId>
        <artifactId>log4j</artifactId>
        <version>1.2.17</version>
    </dependency>

</dependencies>
```



**创建实体类 `User.java`** 并生成get,set和tostring方法

```java
public class User {
    private Integer id;
    private String name;
    private Integer age;
    private String email;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
                '}';
    }
}
```

**`UserMapper.java` 接口** 声明方法

```java
public interface UserMapper {
    //查询所有
    List<User> findAll();
}

```



#### 配置文件和mapper映射文件

配置文件配置数据库连接的信息和映射文件的路径，映射文件是写sql语句的

**mybatis-config.xml**

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">

<configuration>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/test?serverTimezone=UTC"/>
                <property name="username" value="root"/>
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>
    <!--    加载核心配置文件-->
    <mappers>
        <mapper resource="com/kinvy/mapper/UserMapper.xml"/>
    </mappers>
</configuration>


```



**映射文件，UserMapper.xml**

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<mapper namespace="com.kinvy.mapper.UserMapper">
    <select id="findAll" resultType="com.kinvy.domain.User">
        select * from user
    </select>
</mapper>
```



#### 其他

为了便于调试，添加log4j配置打印sql语句， `log4j.properties`

```properties
### direct log messages to stdout ###
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.Target=System.out
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d{ABSOLUTE} %5p %c{1}:%L - %m%n

### direct messages to file mylog.log ###
log4j.appender.file=org.apache.log4j.FileAppender
log4j.appender.file.File=c:/mylog.log
log4j.appender.file.layout=org.apache.log4j.PatternLayout
log4j.appender.file.layout.ConversionPattern=%d{ABSOLUTE} %5p %c{1}:%L - %m%n

### set log levels - for more verbose logging change 'info' to 'debug' ###

log4j.rootLogger=debug, stdout

```



#### 测试类

```java
public class MybatisTest {

    @Test
    public void testFindAll() throws IOException {
        //1.读取配置文件
        InputStream inputStream = Resources.getResourceAsStream("mybatis-config.xml");
        //2.创建sqlSeesionFactory工厂
        SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
        SqlSessionFactory factory = builder.build(inputStream);
        //3.使用工厂生产sqlSession连接对象
        SqlSession session = factory.openSession();
        //4.使用sqlSessioni创建Dao接口的代理对象
        UserMapper userMapper  = session.getMapper(UserMapper.class);
        //5.使用代理对象执行方法
        List<User> list = userMapper.findAll();
        System.out.println(list);
        //6.释放资源
        session.close();
        inputStream.close();
    }

}

```



整个文件结构

![image-20211204213347990](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211204213347990.png)







