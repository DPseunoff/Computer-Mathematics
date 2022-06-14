clear all
disp('Введите матрицу А');
A = input('');
disp('Введите столбец b');
B = input('');

%Метод Гаусса
%[-8,5,8,-6; 2,7,-8,-1; -5,-4,1,-6; 5,-9,-2,8]
%[-144;25;-21;103]
n = size(A,1);
M = zeros(n, n+1); %матрица, в которой хранятся А и b
M(1:n, 1:n) = A;  
M(1:n, n+1:n+1) = B;
for i = 1:n-1     %Приведение матрицы к диагональному виду
    if (M(i,i) == 0)  %Замена строк при необходимости
        temp = M(i:i, 1:n+1);
        M(i:i,1:n+1) = M(i+1:i+1,1:n+1);
        M(i+1:i+1,1:n+1) = temp;
    else
        for j = i+1:n
            x = M(j,i) / M(i,i);
            for k = i:n+1
                M(j,k) = M(j,k) - x*M(i,k);
            end
        end
    end
end
Ans = zeros(n,1);
Ans(n) = M(n,n+1) / M(n,n); %Находим X_n
for i = 1:n-1             %Нахождение остальных Х
    x = M(n-i,n+1);       
    for j=1:i
        x = x - M(n-i,n+1-j) * Ans(n+1-j);
    end
    Ans(n-i) = x / M(n-i,n-i);
end
disp('Результат');
disp(Ans);
