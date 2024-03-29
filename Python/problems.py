#-----------------------------------------------------------------------------
def problem1():
    """
    Multiples of 3 or 5:
    
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    return sum([i for i in range(1000) if (i%3 == 0 or i%5 == 0)])

#-----------------------------------------------------------------------------
def problem2(x):
    """
    Even Fibonacci Numbers:

    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89

    By considering the terms in the Fibonacci sequence whose values do not 
    exceed four million, find the sum of the even-valued terms.
    """
    res, fib1, fib2 = 0, 0, 1
    while(True):
        if (fib2 > x):
            return res
        if (fib2%2 == 0):
            res += fib2
        fib2, fib1 = fib2+fib1, fib2

#-----------------------------------------------------------------------------
def problem3(number):
    """
    Largest Prime Factor:

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 400851475143?
    """
    if (number%2 == 0): number = 2
    larguest, i = 3, 3
    while(True):
        if(number%i == 0):
            number /= i
            larguest = i
        else:
            i += 2
        if(number == 1):
            return larguest

#-----------------------------------------------------------------------------
def problem4():
    """
    Largest Palindrome Product

    A palindromic number reads the same both ways. The largest palindrome made 
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers
    """
    n1, n2 = 999, 100
    palindrome = 0
    for i in range(n1, n2, -1):
        if(i*n1 < palindrome): break
        for j in range(n1, n2, -1):
            if (str(i*j) == str(i*j)[::-1] and i*j > palindrome):
                palindrome = i*j
    return palindrome
#-----------------------------------------------------------------------------
def factors(n):
    v = [0 for i in range(n)]
    i = 2
    while(True):
        if(n%i == 0):
            n /= i
            v[i-1] += 1
        else:
            i += 1
        if(n == 1):
            return v

def merge(v1, v2):
    for i in range(len(v1)):
        if(v1[i] > v2[i]):
            v2[i] = v1[i]
    return v2

def problem5(n):
    """
    Smallest Multiple

    2520 is the smallest number that can be divided by each of the numbers 
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    """
    v = [0 for i in range(n)]
    s = 1
    for i in range(n, 2, -1):
        v = merge(factors(i), v)
    for i in range(len(v)):
        s *=  pow((i+1), v[i])
    return s

#-----------------------------------------------------------------------------
def problem6(n):
    """
    Sum Square Difference

    The sum of the squares of the first ten natural numbers is,

    1^2+2^2+...+10^2 = 385.

    The square of the sum of the first ten natural numbers is,

    (1+2+...+10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten 
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one 
    hundred natural numbers and the square of the sum.
    """
    return pow(sum([i for i in range(n+1)]), 2) - sum([pow(i, 2) for i in range(n+1)])


#-----------------------------------------------------------------------------
def isPrime(n, v):
    for i in v:
        if(n%i == 0):
            return False
    return True

def problem7(n):
    """
    10001st Prime

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10001st prime number?
    """
    v = [2]
    number = 3
    while(True):
        if(len(v) == n):
            return v[n-1]
        if(isPrime(number, v)):
           v.append(number)
        number += 2

#-----------------------------------------------------------------------------
def product(v):
    s = 1
    for i in v:
        s *= i
    return s

def problem8(n):
    string = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    s = 0
    while(True):
        if(len(string) < 13):
            return s
        news = product([int(i) for i in string[0:n]])
        s = s if s > news else news
        string = string[1:]

#-----------------------------------------------------------------------------
def problem9(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if(a*a+b*b == c*c and a+b+c == 1000):
                    return a*b*c

#-----------------------------------------------------------------------------
def problem9(n):
    v = [2]
    for i in range(3, n+1, 2):
        print(i)
        isPrime = True
        for j in v:
            if(i%j == 0):
                isPrime = False
                break
        if(isPrime):
            v.append(i)
    return sum(v)

#-----------------------------------------------------------------------------
def problem11():
    pass

#-----------------------------------------------------------------------------
def problem12():
    pass

#-----------------------------------------------------------------------------
def problem13():
    string ="37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690"
    s = 0
    for i in range(100):
        s += int(string[0:50])
        string =  string[50:]
    return str(s)[0:10]

#-----------------------------------------------------------------------------
def problem14():
    number = 0
    savedIter = 0
    for i in range(1, 1000001):
        iaux = i
        iter = 1
        while(True):
            iter += 1
            if(iaux == 1):
                break
            iaux = (iaux/2) if (iaux%2 == 0) else (3 * iaux + 1)
        if(iter>savedIter):
            savedIter = iter
            number = i
    return number

#-----------------------------------------------------------------------------
def problem15():
    pass

#-----------------------------------------------------------------------------
def problem16():
    return sum([int(i) for i in str(pow(2,1000))])

#-----------------------------------------------------------------------------
def problem17():
    pass

#-----------------------------------------------------------------------------
def problem18():
    pass

#-----------------------------------------------------------------------------
def problem19():
    pass

#-----------------------------------------------------------------------------
def problem20(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return sum([int(i) for i in str(factorial)])

#-----------------------------------------------------------------------------
def problem21():
    pass

#-----------------------------------------------------------------------------
def problem22():
    pass

#-----------------------------------------------------------------------------
def problem23():
    pass

#-----------------------------------------------------------------------------
def problem24():
    pass

#-----------------------------------------------------------------------------
def problem25(n):
    fib1, fib2, index = 1, 1, 2
    while(True):
        index += 1
        fib2, fib1 = fib2+fib1, fib2
        if(len(str(fib2)) == n):
            return index

#-----------------------------------------------------------------------------
def problem26():
    pass

#-----------------------------------------------------------------------------
def problem27():
    pass

#-----------------------------------------------------------------------------
def problem28():
    pass

#-----------------------------------------------------------------------------
def problem29():
    pass

#-----------------------------------------------------------------------------
def problem30():
    """
    We can find out the maximun possible sum for a given number of digits by multiplying
    9^5 by the number of digits. If 9^5 * number of digits < number, wont find any other
    number whitch fullfill the condition
    """
    v = []
    i = 2
    while(True):
        i += 1
        if(i == sum([pow(int(j), 5) for j in str(i)])):
            print(i)
            v.append(i)
        if(pow(9, 5)*len(str(i)) < i):
            break
    return sum(v)

#-----------------------------------------------------------------------------
def problem31():
    pass

#-----------------------------------------------------------------------------
def problem32():
    pass

#-----------------------------------------------------------------------------
def problem33():
    pass

#-----------------------------------------------------------------------------
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac

def factorialSum(vs):
    facSum = 0
    for i in vs:
        facSum += factorial(i)
    return facSum

def problem34(n):
    s = 0
    for i in range(3, n):
        if(i == factorialSum([int(n) for n in str(i)])):
            s += i
    return s

#-----------------------------------------------------------------------------
def problem35():
    pass

#-----------------------------------------------------------------------------
def problem36(n):
    s = 0
    for i in range(n):
        if(str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]):
            s +=i
    return s

#-----------------------------------------------------------------------------
def problem37():
    pass

#-----------------------------------------------------------------------------
def problem38():
    pass

#-----------------------------------------------------------------------------
def problem39():
    pass

#-----------------------------------------------------------------------------
def problem40():
    decimals = ""
    i, product1n = 1, 1
    while(len(decimals) < 1000000):
        decimals = decimals + str(i)
        i += 1
    for i in [10**n for n in range(7)]:
        product1n *= int(decimals[i-1])
    return product1n

#-----------------------------------------------------------------------------
def problem41():
    pass

#-----------------------------------------------------------------------------
def problem42():
    pass

#-----------------------------------------------------------------------------
def problem43():
    pass

#-----------------------------------------------------------------------------
def problem44():
    pass

#-----------------------------------------------------------------------------
def problem45():
    pass

#-----------------------------------------------------------------------------
def problem46():
    pass

#-----------------------------------------------------------------------------
def problem47():
    pass

#-----------------------------------------------------------------------------
def problem48():
    pass

#-----------------------------------------------------------------------------
def problem49():
    pass