Title: Testing File
Date: 2023-09-06 23:46
Category: Post

This is a testing file. Not much to it.

But I am going to write a little so that I can look at how the website is building these types of things. I need to check a lot of the functions that markdown allows for. This is so that I can see how this is being built and how Pelican is building my web content. This is going to be my first post. What I need to go and do next is try an add an image to this. Next link other posts or projects in this one. I need to test lists and charts.


![Local Image]({attach}/repo/assets/gigachad.png)

<img class="center" src="{attach}/repo/assets/gigachad.png" style="max-width: 90%;" ></img>


``` python
from typing import Iterator

# This is an example
class Math:
    @staticmethod
    def fib(n: int) -> Iterator[int]:
        """Fibonacci series up to n."""
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b

result = sum(Math.fib(42))
print("The answer is {}".format(result))
```

``` verilog
module test ();
  assign x = 1'b0;

  always @(posedge clk) begin
    if (x) begin
    end
  end
endmodule
```

This is an `inline test`.

  Testing the indented style


