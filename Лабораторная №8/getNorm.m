function func = getNorm(A)
    func=0;
    for i=1:size(A,2)
        x=0;
        for j=1:size(A,1)
            x=x+abs(A(j,i));
        end
        if(x>func)
            func=x;
        end
    end
end

