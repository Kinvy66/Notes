# C++ 语法技巧



## `!!`

两个逻辑非 `!` 运算符是将非0值转换成1，而0值还是0. 即将数值类型转换为 bool 类型

```cpp
bool FileLogAppender::reopen() {
    if (m_filestream) {
        m_filestream.close();
    }
    m_filestream.open(m_filename);

    return !!m_filestream;
}
```

