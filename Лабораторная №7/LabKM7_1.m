#Заданные данные
yt = @(x,y)(y/x)+(x^2)*sin(x)
y = @(x)x.*sin(x)-(x.^2).*cos(x)+x
y0 = 1.3011687;
a = [1,2];
h = 0.1;

x = a(1):h:a(2);
n = size(x,2);

%Метод Эйлера
YE = zeros(1,n);
YE(1) = y0;
for i = 2:n
   YE(i) = YE(i-1) + h * yt(x(i-1),YE(i-1));
end

%Метод Эйлера c пересчетом
YEP = zeros(1,n);
YEP(1) = y0;
for i = 2:n
   tmp = YEP(i-1) + h * yt(x(i-1),YEP(i-1));
   YEP(i) = YEP(i-1) + h * (yt(x(i-1),YEP(i-1)) + yt(x(i),tmp)) / 2;
end

%Метод Рунге-Кутты
YR = zeros(1,n);
YR(1) = y0;
for i = 2:n
   k1 = yt(x(i-1),YR(i-1));
   k2 = yt(x(i-1) + h/2, YR(i-1) + h*k1/2);
   k3 = yt(x(i-1) + h/2, YR(i-1) + h*k2/2);
   k4 = yt(x(i-1) + h,YR(i-1) + h*k3);
   YR(i) = YR(i-1) + h * (k1+2*k2+2*k3+k4)/6;
end

%Метод Адамса
YA = zeros(1,n);
YA(1) = y0;
for i = 2:3
   k1 = yt(x(i-1),YA(i-1));
   k2 = yt(x(i-1) + h/2, YA(i-1) + h*k1/2);
   k3 = yt(x(i-1) + h/2, YA(i-1) + h*k2/2);
   k4 = yt(x(i-1) + h, YA(i-1) + h*k3);
   YA(i) = YA(i-1) + h * (k1+2*k2+2*k3+k4)/6;
end
for i = 4:size(x,2)   
    YA(i) = YA(i-1) + h/12*(23*yt(x(i-1), YA(i-1)) - 16*yt(x(i-2),YA(i-2)) + 5*yt(x(i-3),YA(i-3)));
end

#Вывод графиков
hold on
subplot(2,2,1)
plot(x, y(x), x, YE)
title('Метод Эйлера');
legend('Точное','Приближенное')
xlabel('x')
ylabel('y')

subplot(2,2,2)
plot(x, y(x), x, YEP)
title('Метод Эйлера c пересчётом');
legend('Точное','Приближенное')
xlabel('x')
ylabel('y')

subplot(2,2,3)
plot(x, y(x), x, YR)
title('Метод Рунге-Кутты');
legend('Точное','Приближенное')
xlabel('x')
ylabel('y')

subplot(2,2,4)
plot(x, y(x), x, YA)
title('Метод Адамса');
legend('Точное','Приближенное')
xlabel('x')
ylabel('y')
