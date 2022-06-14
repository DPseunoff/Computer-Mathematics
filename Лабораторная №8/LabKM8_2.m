clear all
disp('Введите матрицу А');
A = input('');
disp('Введите столбец b');
B = input('');

%Метод прогонки
%[10,-1,0,0,0; -8,16,1,0,0; 0,6,-16,6,0; 0,0,-8,16,-5; 0,0,0,5,-13]
%[16;-110;24;-3;87]

n = size(A,1);
P = zeros(1,n);
Q = zeros(1,n);
P(1) = -A(1,2)/A(1,1);
Q(1) = B(1)/A(1);
for i = 2:n-1
    P(i)=-A(i,i+1) / (A(i,i) + A(i,i-1) * P(i-1));
    Q(i)=(B(i) - A(i,i-1) * Q(i-1)) / (A(i,i) + A(i,i-1) * P(i-1));
end
Q(n)=(B(n) - A(n,n-1) * Q(n-1))/(A(n,n) + A(n,n-1)*P(n-1));
Ans = zeros(n,1);
Ans(n) = Q(n);
for i=1:n-1
    Ans(n-i)=P(n-i) * Ans(n-i+1)+Q(n-i);
end
disp(Ans);
