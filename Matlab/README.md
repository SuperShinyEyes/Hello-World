```Matlab
1 ~= 2      % 1
xor(1, 0)   % 1
a = pi      %  3.1416
>> format long
>> a        % 3.141592653589793

```

## Vectors
```
>> A = [1 2; 3 4;5 4]
A =
     1     2
     3     4
     5     4


 >> sz = size(A)
 sz =
      3     2


>> sz = size(A, 1)    % First column
sz =
     3


>> length([1;2;3;4;5;6])
ans =
     6


>> v = 1:0.1:2
 v =
   Columns 1 through 6
     1.0000    1.1000    1.2000    1.3000    1.4000    1.5000
   Columns 7 through 11
     1.6000    1.7000    1.8000    1.9000    2.0000


 >> ones(3,4)
 ans =
      1     1     1     1
      1     1     1     1
      1     1     1     1


>> ones(3,4)
ans =
     1     1     1     1
     1     1     1     1
     1     1     1     1


>> rand(1,3)
ans =
    0.8147    0.9058    0.1270


>> randn(1,3)     % Gaussian distribution
ans =
    0.8622    0.3188   -1.3077


>> I = eye(4)   % identity matrix
I =
     1     0     0     0
     0     1     0     0
     0     0     1     0
     0     0     0     1



>> A = eye(5)
A =
     1     0     0     0     0
     0     1     0     0     0
     0     0     1     0     0
     0     0     0     1     0
     0     0     0     0     1

>> A(2,:)       % Access with slice
ans =
     0     1     0     0     0

>> A(2,1:4)
ans =
     0     1     0     0

>> A([1,4],:)   % Access multiple rows
ans =
     1     0     0     0     0
     0     0     0     1     0


>> A([1],:) = [5 5 5 5 5]   % Assign a row
A =
     5     5     5     5     5
     0     1     0     0     0
     0     0     1     0     0
     0     0     0     1     0
     0     0     0     0     1

>> A = [A, [3;3;3;3;3]]     % Expand with a vector
A =
     5     5     5     5     5     3
     0     1     0     0     0     3
     0     0     1     0     0     3
     0     0     0     1     0     3
     0     0     0     0     1     3


>> [1 1; 2 2]
ans =
     1     1
     2     2

>> ans(:)     % Append column vectors into a single one
ans =
     1
     2
     1
     2

>> [eye(2), eye(2)]   % Concatenate matrices
ans =
     1     0     1     0
     0     1     0     1

>> [eye(2) ; eye(2)]  % Concatenate matrices
ans =
     1     0
     0     1
     1     0
     0     1
```

![histogram](/images/matlab_histogram.png)
```
>> hist(rand(1,1000), 100)
```


## Moving around
```
>> pwd
ans =
/Users/young/Documents/MATLAB


>> whos
  Name      Size            Bytes  Class     Attributes

  A         3x2                48  double              
  I         4x4               128  double              
  a         1x1                 8  double              
  ans       1x22               44  char                
  c         1x3                24  double              
  sz        1x1                 8  double              
  v         1x11               88  double              


>> load file.mat

>> save hello.mat variable

>> save hello.txt variable -ascii   % save
```

## Computation
```
>> A = [1 2; 3 4; 5 6]
A =
     1     2
     3     4
     5     6

>> B = [3 3; 1 2;4 4]
B =
     3     3
     1     2
     4     4

>> C = [2 2; 3 1]
C =
     2     2
     3     1

>> A .* B       * element-wise
ans =
     3     6
     3     8
    20    24

>> A .^ 2       * element-wise
ans =
     1     4
     9    16
    25    36

>> K = [1;2;3]
>> 1 ./ K
ans =
    1.0000
    0.5000
    0.3333

>> abs(K)
>> exp(K)
>> log(K)
>> -K
>> [val, index] = max(K)
>> sum(K)
>> prod(K)
>> floor(K)
>> ceil(K)
>> pinv(K)    % invert

>> a = [1 2 3 4]
>> a < 3
ans =
  1×4 logical array
   1   1   0   0

>> find(a <3)
ans =
    1     2

>> M = magic(4)      % Sudoku matrix
M =
    16     2     3    13
     5    11    10     8
     9     7     6    12
     4    14    15     1


>> [row, col] = find(M >= 15)
row =
     1
     4
col =
     1
     3


>> a1 = [1 2;1 2]
a1 =
     1     2
     1     2

>> a2 = [2 1;2 1]
a2 =
     2     1
     2     1

>> max(a1, a2)
ans =
     2     2
     2     2


>> A
A =
     1     2
     3     4
     5     6
>> max(A, [], 1)    % == max(A)
ans =
     5     6
>> max(A, [], 2)
ans =
      2
      4
      6
>> max(A(:)) == max(max(A))


>> M = magic(3)
M =
     8     1     6
     3     5     7
     4     9     2

>> sum(M)     % == sum(M, 1)
ans =
    15    15    15

>> sum(M, 2)
ans =
    15
    15
    15

>> sum(sum(M .* eye(size(M))))    % diagonal sum
ans =
    15

>> sum(sum(M .* flipud(eye(size(M)))))    % diagonal sum
ans =
    15

```
## Plot
![plot sin](/images/matlab_plot.png)
```
>> t = [0:0.01:1];
>> y1 = sin(2*pi*5*t);
>> plot(t, y1)
```
![plot sin](/images/matlab_plot2.png)
```
>> y2 = cos(2*pi*5*t)/2;
>> hold on
>> plot(t, y2, 'r')
>> xlabel('time')
>> ylabel('value')
>> legend('sin', 'cos')
>> title('the plot')
>> print -dpng 'plot.png'
>> close      % close figure
```
![plot sin](/images/matlab_plot3.png)
```
>> figure(1); plot(t, y1);
>> figure(2); plot(t, y2);
>> subplot(1,2,1);
>> plot(t, y1)
>> subplot(1,2,2);
>> plot(t, y2)
>> axis([0.5, 1, -1, 1])    % Change range in plot
```
![plot sin](/images/matlab_plot4.png)
```
>> A = magic(5)
A =
    17    24     1     8    15
    23     5     7    14    16
     4     6    13    20    22
    10    12    19    21     3
    11    18    25     2     9
>> imagesc(A), colorbar, colormap gray
```

## For-loop, while
```
>> v = zeros(5, 1)
v =
     0
     0
     0
     0
     0

>> for i = 1:5,
v(i) = 2 ^ i;
end;

>> v
v =
     2
     4
     8
    16
    32

>> i = 1;
>> while true,
    v(i) = 123;
    i = i + 1;
    if i == 3,
        break;
    end;
end;
>> v
v =
   123
   123
     8
    16
    32
```

## functions
```
function J = costFunctionJ(X, y, theta)

m = size(X, 1);             % num of training examples
predictions = X * theta;    % predictions of hypothesis on all m examples
sqrErrors = (predictions - y) .^ 2;
                            % squared errors

J = 1 / (2*m) * sum(sqrErrors)
```
##
```
```
##
```
```
##
```
```
##
```
```
##
```
```
##
```
```
