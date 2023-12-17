# problem 1
calculatePower :: Int -> Int -> Int
calculatePower _ 0 = 1
calculatePower base exp = base * calculatePower base (exp - 1)

# problem 2
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

# problem 3
applyFunction :: (Int -> Int) -> [Int] -> [Int]
applyFunction _ [] = []
applyFunction f (x:xs) = f x : applyFunction f xs

# problem 4
main :: IO ()
main = do
    putStrLn "Enter a base:"
    base <- readLn :: IO Int
    putStrLn "Enter an exponent:"
    exp <- readLn :: IO Int
    let powerResult = calculatePower base exp
    putStrLn $ "Result of raising the base to the exponent: " ++ show powerResult
    
    putStrLn "Enter a non-negative integer:"
    num <- readLn :: IO Int
    let factorialResult = factorial num
    putStrLn $ "Factorial of the entered integer: " ++ show factorialResult
    
    putStrLn "Enter a list of integers separated by commas:"
    input <- getLine
    let numbers = map read $ wordsWhen (== ',') input :: [Int]
    let appliedFunction = applyFunction (\x -> x * x) numbers
    putStrLn $ "Applied function results: " ++ show appliedFunction

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

# problem 5
isPalindrome :: String -> Bool
isPalindrome [] = True
isPalindrome [_] = True
isPalindrome (x:xs)
    | x == last xs = isPalindrome (init xs)
    | otherwise = False

# problem 6
fibEven :: Int -> [Int]
fibEven 0 = [0]
fibEven n = 0 : [x | x <- fibOdd (n - 1)]

fibOdd :: Int -> [Int]
fibOdd 0 = [1]
fibOdd n = 1 : [x + y | (x, y) <- zip (fibEven (n - 1)) (fibOdd (n - 1))]

main :: IO ()
main = do
    putStrLn "Enter the value of n to generate the Fibonacci sequence up to the nth term:"
    n <- readLn :: IO Int
    let fibSequence = take n (fibEven n)
    putStrLn $ "Fibonacci sequence up to the nth term: " ++ show fibSequence
