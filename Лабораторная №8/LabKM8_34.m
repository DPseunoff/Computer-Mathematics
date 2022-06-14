clear all
disp('Введите матрицу А');
A = input('');
disp('Введите столбец B');
B = input('');

%Метод простых итераций
%[15,7,0,5; -3,-14,-6,1; -2,9,13,2; 4,-1,3,9]
%[176;-111;74;76]
n = size(A,1);
for i = 1:n
    if (A(i,i) == 0)
        if (i == n)
            temp = A(i:i,1:n);
            A(i:i,1:n) = A(1:1,1:n);
            A(1:1,1:n) = temp;
        else
            temp = A(i:i,1:n);
            A(i:i,1:n) = A(i+1:i+1,1:n);
            A(i+1:i+1,1:n) = temp;
        end
    end
end
for i = 1:n
    x = A(i,i);
    for j = 1:n
        A(i,j) = -A(i,j)/x;
    end
    B(i) = B(i)/x;
    A(i,i) = 0;
end
PrevAns1 = B;
Ans1 = A * PrevAns1 + B;
k = 1;
eps = 0.01;
while (getNorm(Ans1-PrevAns1) > eps)
    PrevAns1 = Ans1;
    Ans1 = A * PrevAns1 + B;
    k = k + 1;
end
disp(strcat('Метод простых итераций. Кол-во итераций: ', num2str(k)));
disp(Ans1);

%Метод Зейделя
PrevAns2 = B;
Ans2 = PrevAns2;
for i = 1:n
    Ans2(i) = A(i:i,1:n) * Ans2 + B(i);
end
k=1;
eps=0.01;
while (getNorm(Ans2-PrevAns2) > eps)
    PrevAns2 = Ans2;
    for i = 1:n
        Ans2(i) = A(i:i,1:n) * Ans2 + B(i);
    end
    k = k+1;
end
disp(strcat('Метод Зейделя. Количество иетарций: ', num2str(k)));
disp(Ans2);
