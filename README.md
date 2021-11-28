## Codewars



### Beginner Series1_School Paperwork



### Beginner Series2_clock



### Beginner Series3_sum of Numbers



### Beginner Series4_Cockroach



### Beginner Series5_Triangular Numbers

[题目链接](https://www.codewars.com/kata/56d0a591c6c8b466ca00118b)

这里取了个巧，先根据公式进行简化，找到大致范围的最小值和最大值，这样区间相对于原来的数量级变小，然后使用循环判断赋值即可。__这里注意在函数、方法等用法时，如果结束未使用return，会返回None，因此这里采用a赋值再输出避免None的出现。__

### Detect Pangram

[题目链接](https://www.codewars.com/kata/545cedaa9943f7fe7b000048)

先将字母均转化为小写减少计算量，然后循环遍历并与字母表对比，如果不在字母表即退出循环。

``string.ascii_lowercase``是[``string``库](https://docs.python.org/zh-cn/3/library/string.html)的小写字母字符串。

```
string库部分节选
string.ascii_lowercase				## 小写字母字符串
string.ascii_uppercase				## 大写字母字符串
string.ascii_letters				## 小写和大写字母字符串
string.digits						## 数字字符串
string.hexdigits					## 十六进制字符串0-F
string.octdigits					## 八进制字符串0-7
```

### Multiples of 3 or 5

[题目链接](https://www.codewars.com/kata/514b92a657cdc65150000006)

比较简单、粗暴的解法，先判断是否``int``型，然后for循环得到3、5对应倍数的数，用``three_number``和``five_number``累计最后相加即可。



### Sentence to words

[题目链接](https://www.codewars.com/kata/57a05e0172292dd8510001f7)

其实可以直接用split分隔然后转为列表，但作为练习自己试了一下。

基本思路是通过for遍历字符串，出现空格就将这一段s[j:i]作为加入，当进行到末尾时，附加最后一段即可。



### ToLeetSpeak

[题目链接](https://www.codewars.com/kata/57c1ab3949324c321600013f)

创建一个元组记录替换的结果，由于这个题目所涉及的字符串均为大写字母且正序，所以用ascii码判断是否在65-90范围内判断后直接替换即可。

### Break camelCase

[题目链接](https://www.codewars.com/kata/5208f99aee097e6552000148)

这个题目更像是命名规范的驼峰式转化~~，for循环遍历，如果非大写字母正常附加，如果是大写字母，先添加空格再添加字符。

### Who likes it

[题目链接](https://www.codewars.com/kata/5266876b8f4bf2da9b000362)

``if elif else``依次判断即可，注意两个人及以上时候结果有所不同，需要调整内容即可。



### Build a pile of Cubes

[题目链接](https://www.codewars.com/kata/5592e3bd57b64d00f3000047)

取了一下巧，根据$n^3 + (n-1)^3 + ... + 1^3 = m$公式可以得到一个大致的范围$[n^4/8, n^4/2]$，反过来，得到最后的结果在n的范围$[\sqrt[4]{2m},\sqrt[4]{8m}]$，因此在这个范围内进行循环，再将结果与m对比即可确定是否由n这个数量的立方体。



### Words to sentence

[题目链接](https://www.codewars.com/kata/57a06005cf1fa5fbd5000216)

这里使用for循环让数组里面的数据不断叠加到字符串中并添加空格，最后去掉末尾的空格。



### Moving Zeros To The End

[题目链接](https://www.codewars.com/kata/52597aa56021e91c93000cb0)

由于只需要将0移到末尾，所以先通过for对原列表循环得到原列表非0的新列表和列表内0的个数，然后循环将0再依次添加最后即可。



### Roman Numerals Decoder

[题目链接](https://www.codewars.com/kata/51b6249c4612257ac0000005)

罗马字符转为阿拉伯数字，用for对字符循环，依次与M、D、C、L、X、V、I判断，如果等于加上对应的值，由于还有CM、CD类型的存在，当这种出现为了避免与C、D、M重复计算，采用减法的方式，如M为1000、CM为900，这样CM可以计算为+1000-100，不仅能避免重复计算，还能显得简洁一些。

### Scramblies

[题目链接](https://www.codewars.com/kata/55c04b4cc56a697bb0000048)

先采用if进行比较大小，然后以较短的字符进行循环，如果较短的字符串内的字符均在另一个字符串内，说明构成元素基本相似，但存在元素相似但数量存在差异，所以对比字符的数量，如果较小的字符串内的字符能保证元素、数量均在较大的字符串内体现，即为符合。



### Where my anagrams at

[题目链接](https://www.codewars.com/kata/523a86aa4230ebb5420001e1)

由于存在列表，所以先使用列表进行循环，依次比较，因为是存在“相同的字母”，所以第一步先排除字符串内字母长度不等的元素，由于可能存在字符串很长的情况（如果以字符串进行比较，存在运行时间过长的情况），所以以字母进行比较，26个字母，一个字符串最多比较26次，``^``为二进制计算符，两者相同才为True，即可确定两个字符串是否相同。



### Roman Numerals Helper

[题目链接](https://www.codewars.com/kata/51b66044bce5799a7f000003)

罗马数字转阿拉伯数字可参考Roman Numerals Decoder，这里简化了一下，创建了一个列表简化了公式，

阿拉伯数字转罗马数字通过``while``循环，从高位一次比对大小，直至数字减为0，得到结果。



### Sum of Intervals

[题目链接](https://www.codewars.com/kata/52b7ed099cdc285c300001cd)

这个简单，可能是排错难度了，两层for循环、一个if判断是否重复获得所有的值累加即可得到结果。



### Nesting Structure Comparison

[题目链接](https://www.codewars.com/kata/520446778469526ec0000001)

这道题相对来说在4kyu比较难，列表的嵌套没有定义最高多少，因此在``same_structure_as``先进行基本的列表判断和最外层列表判断，如果比对过程中出现嵌套列表，则进入``string_to_list``进行循环处理，如果出现两层以上的嵌套列表，再次进入``string_to_list``进行循环处理。比对单层列表时，用``len()``判断元素数量和``type()``判断元素类型。

```
isinstance(object, classinfo)		
##判断object是否为classinfo类型，classinfo类型包括基本类型、类名、以及它们组成的元组
```



### Smallest possible sum

[题目链接](https://www.codewars.com/kata/52f677797c461daaf7000740)

这个题目虽然是4kyu，但更多是考察数学能力，因为n个数相减，最后的结果是n个数的公约数，所以使用``if``判断列表内元素格式讨论，如果高于2个开始``for``循环，依次求公约数，如果公约数已经为1（最小的公约数了），就得到最后的列表的数，最小公约数乘以列表元素数量即为结果。



```
import math
math.ceil(x)				## x的最小整数，x的上限
math.floor(x)				## x的最小整数，x的下限
math.fabs(x)				## x的绝对值
math.gcd(x1,x2,x3...)		## 最大公约数
math.lcm(x1,x2,x3...)		## 最大公倍数
math.isfinite(x)			## x非无穷大也非NaN返回True
math.isinf(x)				## x为无穷大返回True
math.isnan(x)				## x为NaN返回True
math.modf(x)				## 返回x的小数和整数部分
math.pow(x, y)				## x的y次幂
math.sqrt(x)				## x的平方根
math.isqrt(x)				## 返回x的整数平方根，向下取整


math.pi						# π
math.e						# e
math.exp(x)					## e的x次幂
math.log(x)					## 底为e时x的对数
math.log2(x)				## 底为2时x的对数
math.log10(x)				## 底为10时x的对数
math.asin(x)				## x的反正弦值
math.atan(x)				## x的反正切值
math.sin(x)					## x的正弦值
math.tan(x)					## x的正切值
......
```



### Ten-Pin Bowling

[题目链接](https://www.codewars.com/kata/5531abe4855bcc8d1f00004c)

``pin``代表局数，``pin_score``得到基本分数，``if``分情况讨论，如果出现``/``（即为spare，本局第二次投掷命中剩下的）且非末局，加上下一次的分数；如果出现``X``（即为一次全部击倒）且非末局，增加后两次的分数。



### Breadcrumb Generator

[题目链接](https://www.codewars.com/kata/563fbac924106b8bf7000046)

这里用到了正则，先提取网站网址（www.xxx.xx）、目录内容（\xx\xxxx\xxx\）、尾端（xxx.html/htm），然后通过for循环依次获得目录内容的各个目录。

当然实际更复杂，网址存在很多形式（需要改正则）、目录内容可能为0、尾端需要缩写（取开头字母并排除给定的内容）、尾端可能存在不同形式。



### Most frequently used words in a text

[题目链接](https://www.codewars.com/kata/51e056fe544cf36c410000fb)





### Calculator_Retired

这个[题目](https://www.codewars.com/kata/5235c913397cbf2508000048)已经Retired了，可能是因为这个计算器的实现出现floor的问题，依旧写下目前的解法。

``step``作为一层算式的计算，每一层算式计算中，先获取``*、/``这种优先级高的算式，给予``basic_calc_str``计算，替换原来的算式，然后在对``+、-``这种进行计算，如果是``(xx)``这种类型，去除括号，如果一层循环结束后存在``()``，说明算式为多层循环，调用``step``继续循环。``basic_calc_str``计算中需要以float进行计算，避免int与float计算出现极限值。



### Codewars style ranking system

[题目链接](https://www.codewars.com/kata/51fda2d95d6efda45e00004e)

由于等级范围确定，所以建立一个``rank_range``列表来记录等级范围方便循环取值，``inc_progress``记录挑战题目时的情况，不同等级差``if``分类讨论得到分数情况即可，当progress超过升级分数时且自身等级仍在预定义范围内时，进入``rank_new``函数，由于可能存在升级后大于预定义等级范围内，所以将这种情况进入``rank_top``函数，等级归为最高，且progress为0。

``rank_new``循环中注意与等级列表范围的对应情况。



### Strings Mix

[题目链接](https://www.codewars.com/kata/5629db57620258aa9d000014)

先获取两个字符串的各个字母和个数，``list_all``为两个字符串的字母总和，进行循环，当第一个字符串大于第二个字符串且第一个字符串出现次数大于1时，用列表添加结果，此时已经获得两个字符串不同之处，然后用``sorted``排序，记得按照长度、字母排序``sorted(result, key=lambda item: (-len(item), item))``，最后转化为字符串去除末尾``/``即可。



### The Lift

[题目链接](https://www.codewars.com/kata/58905bfa1decb981da00009e)

难度极为高的一道题。

基本思路是采用了for循环对上升过程的层级进行遍历，如果存在上升的人判断是否超员然后进入下一层，并记录该层。下降过程亦如此。由于存在多次上升下降，``Lift_on``为一次上升下降的情况，多次上升下降反复调用即可。

变量中要考虑每一个上升下降循环经过的层级、每一个上升下降循环后的电梯情况、每一层的人数情况、一次上升/下降出现重复值的情况等等，所以显得很麻烦。



------------------

在完成The Lift这道题后，我升到了4kyu了，解锁了可以上传题目的权限，而python对应的更高等级的题目也随之变得不多，因此我考虑写了一段刷题的总结，有可能后面不会再高强度的刷codewars题目了。





