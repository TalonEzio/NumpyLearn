import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

def numpyArrayWithCondition(condition,source:np.ndarray) -> np.ndarray:
    return np.array(
        list(
            map(condition,source)
        )
    )
def numpyAnyWithCondition(condition,source:np.ndarray) ->bool:
    return np.any(
          list(map(condition,source))
      )
def numpyAllWithCondition(condition,source:np.ndarray) ->bool:
    return np.all(
          list(map(condition,source))
      )

#Test whether none of the elements of a given array is zero
x = np.array([1, 2, 3, 4])
y = np.array([0, 6, 7, 8])

print('Test whether none of the elements of a given array is zero')
print(x,'-->',x.all(0))
print(y,'-->',numpyAllWithCondition(lambda i: i != 0,y))

#Test a given array element-wise for finiteness (not infinity or not a Number)
x = np.array([1,2,3,np.nan,np.inf])
print('Test whether none of the elements of a given array')
print(x,'-->',numpyArrayWithCondition(lambda i: not (np.isinf(i) or np.isnan(i)),x))

#print(np.isfinite(x))# simple 😂😂😂
#Test element-wise for positive or negative infinity.
x = np.array([1,2,3,np.nan,np.inf])
print('Test element-wise for positive or negative infinity.')
print(x,'-->',numpyArrayWithCondition(lambda i: np.isinf(i),x))

#print(np.isinf(x))# simple 😂😂😂

#Test element-wise for NaN of a given array
print('Test element-wise for NaN of a given array')
x = np.array([1,2,3,np.nan,np.inf])
print(x,'-->',numpyArrayWithCondition(lambda i: np.isnan(i),x))


print(np.isnan(x))

#Test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not
x = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print('Test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not')
print(x)
print('--> complex:', numpyArrayWithCondition(np.iscomplex, x)) #LOL
print('--> complex:', np.iscomplex(x))
print('--> real:', np.isreal(x))
print('--> scalar:', np.isscalar(x))

#Test whether two arrays are element-wise equal within a tolerance
print('Test whether two arrays are element-wise equal within a tolerance')
x = [1.0, np.nan]
y = [1.0, np.nan]
merge = [x,y]
#no custom solution 😒


