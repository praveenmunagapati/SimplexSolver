from simplex import SimplexSolver
from fractions import Fraction
import unittest


class SimplexSolverTest(unittest.TestCase):

    ''' STANDARD FORM MAXIMIZATION EXAMPLES '''
    def test_max_feasible1(self):
        ''' Find optimal solution to max(x1 + x2) such that:
            Ax <= b,
            x1, x2 >= 0,
            A =  |2 1|, b = |4|, c = |1|
                 |1 2|      |3|      |1|

            Source: http://mat.gsia.cmu.edu/classes/QUANT/NOTES/chap7.pdf
                    Example 7.2.1
        '''
        self.assertDictEqual({'x0': Fraction(5,3),
                              'x1': Fraction(2,3),
                              's0': Fraction(0),
                              's1': Fraction(0),
                              'opt': Fraction(7,3)},
                              SimplexSolver().run_simplex([[2,1],
                                                           [1,2]],
                                                          [4,3],
                                                          [1,1]))

    def test_max_feasible2(self):
        ''' Find optimal solution to max(4x1 + 6x2) such that:
            Ax <= b,
            x1, x2 >= 0,
            A =  |-1 1|, b = |11|, c = |4|
                 | 1 1|      |27|      |6|
                 | 2 5|      |90|

            Source: http://college.cengage.com/mathematics/larson/elementary_linear/4e/shared/downloads/c09s3.pdf
                    Example 1
        '''
        self.assertDictEqual({'x0': Fraction(15),
                              'x1': Fraction(12),
                              's0': Fraction(14),
                              's1': Fraction(0),
                              's2': Fraction(0),
                              'opt': Fraction(132)},
                              SimplexSolver().run_simplex([[-1,1],
                                                           [1,1],
                                                           [2,5]],
                                                          [11,27,90],
                                                          [4,6]))

    def test_max_feasible3(self):
        ''' Find optimal solution to max(2x1 - x2 + 2x3) such that:
            Ax <= b,
            x1, x2 >= 0,
            A =  |2 1  0|, b = |10|, c = | 2|
                 |1 2 -2|      |20|      |-1|
                 |0 1  2|      | 5|      | 2|

            Source: http://college.cengage.com/mathematics/larson/elementary_linear/4e/shared/downloads/c09s3.pdf
                    Example 2
        '''
        self.assertDictEqual({'x0': Fraction(5),
                              'x1': Fraction(0),
                              'x2': Fraction(5,2),
                              's0': Fraction(0),
                              's1': Fraction(20),
                              's2': Fraction(0),
                              'opt': Fraction(15)},
                              SimplexSolver().run_simplex([[2,1,0],
                                                           [1,2,-2],
                                                           [0,1,2]],
                                                          [10,20,5],
                                                          [2,-1,2]))

    def test_max_feasible4(self):
        ''' Find optimal solution to max(2x1 - x2 + 2x3) such that:
            Ax <= b,
            x1, x2, x3 >= 0,
            A =  |4 1 1|, b = |30|, c = |3|
                 |2 3 1|      |60|      |2|
                 |1 2 3|      |40|      |1|

            Source: http://college.cengage.com/mathematics/larson/elementary_linear/4e/shared/downloads/c09s3.pdf
                    Example 3
        '''
        self.assertDictEqual({'x0': Fraction(3),
                              'x1': Fraction(18),
                              'x2': Fraction(0),
                              's0': Fraction(0),
                              's1': Fraction(0),
                              's2': Fraction(1),
                              'opt': Fraction(45)},
                              SimplexSolver().run_simplex([[4,1,1],
                                                           [2,3,1],
                                                           [1,2,3]],
                                                          [30,60,40],
                                                          [3,2,1]))

    def test_max_feasible5(self):
        ''' Find optimal solution to max(11x1 + 16x2 + 15x3) such that:
            Ax <= b,
            x1, x2, x3 >= 0,
            A =  | 1   2  3/2|, b = |12000|, c = |11|
                 |2/3 2/3  1 |      | 4600|      |16|
                 |1/2 1/3 1/2|      | 2400|      |15|

            Source: http://college.cengage.com/mathematics/larson/elementary_linear/4e/shared/downloads/c09s3.pdf
                    Example 4
        '''
        self.assertDictEqual({'x0': Fraction(600),
                              'x1': Fraction(5100),
                              'x2': Fraction(800),
                              's0': Fraction(0),
                              's1': Fraction(0),
                              's2': Fraction(0),
                              'opt': Fraction(100200)},
                              SimplexSolver().run_simplex([[1,2,Fraction(3,2)],
                                                           [Fraction(2,3),
                                                            Fraction(2,3),1],
                                                           [Fraction(1,2),
                                                            Fraction(1,3),
                                                            Fraction(1,2)]],
                                                          [12000,4600,2400],
                                                          [11,16,15]))

if __name__ == '__main__':
    unittest.main()
