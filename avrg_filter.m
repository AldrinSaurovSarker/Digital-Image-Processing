A = imread('rose.jpg');
x = rgb2gray(A);
B=double(x);

m=input('Enter the value of kernel: ');
k=ones(m)/(m*m);

[r,c] = size(B);

BB=zeros([r+(m-1),c+(m-1)]);
[p,q]=size(BB);

for i=(m+1)/2 : p-((m-1)/2)
    for j=(m+1)/2 : q-((m-1)/2)
        BB(i,j) = B(i-((m-1)/2),j-((m-1)/2));
    end
end

I=zeros([p-(m-1),q-(m-1)]);

str=(m+1)/2;
stc=(m+1)/2;
enr=p-((m-1)/2);
enc=q-((m-1)/2);

for i=str:enr
    for j=stc:enc
       wd=BB(((i-((m-1)/2)):i+((m-1)/2)),((j-((m-1)/2)):j+((m-1)/2)));
       I((i-((m-1)/2)),(j-((m-1)/2)))=sum(wd.*k,'all');
    end
end

I=uint8(I);
subplot(1,2,1);imshow(uint8(B));title('Before');
subplot(1,2,2);imshow(I);title('After ');





