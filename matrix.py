from manim import *
class matrix(Scene):
    def construct(self):
        
        # matrix determinant animation
        matdet = Text("Matrix Determinant",font="Monospace").scale(1)
        
        m0 = Matrix([[8, 4, 3], [-5, 6, -2], [7, 9, -8]]) 
        v = MathTex('x = ').next_to(m0, LEFT)
        mat = VGroup(m0, v).scale(1.5)
        
        self.play(Write(matdet),run_time = .8)
        self.play(Unwrite(matdet),run_time = .8)
        self.play(FadeIn(mat))
        self.play(mat.animate.scale(.65).to_corner(UP))
        m0.save_state()    #saving the state of the variable so it can be restored whenever we want
        
        plus1 = MathTex("+").next_to(m0[0][0],UP)
        minus1 = MathTex("-").next_to(m0[0][1],UP*1.5)
        plus2 = MathTex("+").next_to(m0[0][2],UP)
        signs = VGroup(plus1, minus1, plus2)
        self.play(FadeIn(signs))
        signs.save_state()
        self.play(signs.animate.set_color('#58FF7A00'), run_time = 0.4)
        
        detsign = MathTex(r"\lambda = ").to_corner(LEFT).shift(RIGHT)
        self.play(Write(detsign),run_time = 0.4)
        num8 = m0[0][0].copy()
        
        self.play(
            m0[0][0].animate.set_color("#58FF7A00"),
            num8.animate.next_to(detsign),
            signs[1:].animate.set_color(WHITE),
            run_time = 0.4
            )
        line1 = Line(UP,DOWN).scale(.7).next_to(num8).shift(DOWN * .2)
        line2 = Line(UP,DOWN).scale(.7).next_to(num8,buff=2.5).shift(DOWN * .2)
        self.play(FadeIn(line1,line2), run_time = 0.4)
        
        
        self.play(
            m0[0][1:3].animate.set_color("#949494FF"),
            m0[0][3].animate.set_color("#949494FF"),
            m0[0][6].animate.set_color("#949494FF"),
            run_time = 0.4
        )
        num6 = m0[0][4].copy()
        numneg2 = m0[0][5].copy()
        num9 = m0[0][7].copy()
        numneg8 = m0[0][8].copy()
        self.play(
            num6.animate.next_to(line1).shift(UP * .4),
            numneg2.animate.next_to(line2,LEFT).shift(UP * .4),
            num9.animate.next_to(line1).shift(DOWN * .4),
            numneg8.animate.next_to(line2,LEFT).shift(DOWN * .4), run_time = 0.4
        )
        self.play(
            m0.animate.restore(),
            signs.animate.restore(), run_time = 0.4
            )
        self.play(
            signs[1].animate.set_color("#58FF7A00"),
            m0[0][1].animate.set_color("#58FF7A00"), run_time = 0.4
        )
        minus1copy = minus1.copy()
        self.play(
            minus1copy.animate.next_to(line2).set_color(WHITE).shift(UP * .3), run_time = 0.4
        )
        copy4 = m0[0][1].copy()
        self.play(copy4.animate.next_to(minus1copy).shift(LEFT * .15).set_color(WHITE), run_time = 0.4)
        
        
        self.play(
            m0[0][0].animate.set_color("#949494FF"),
            m0[0][2].animate.set_color("#949494FF"),
            m0[0][4].animate.set_color("#949494FF"),
            m0[0][7].animate.set_color("#949494FF"), run_time = 0.4
        )
        l3 = line1.copy().next_to(copy4).shift(DOWN * .3 + LEFT * .1)
        l4 = line2.copy().next_to(l3,buff=2.5).shift(LEFT * .2)
        self.play(
            FadeIn(l3,l4), run_time = 0.4
        )
        
        numneg5 = m0[0][3].copy()
        numneg2_2 = m0[0][5].copy()
        num7 = m0[0][6].copy()
        numneg8_2 = m0[0][8].copy()
        self.play(
            numneg5.animate.next_to(l3).shift(UP * .4),
            numneg2_2.animate.next_to(l4,LEFT).shift(UP * .4),
            num7.animate.next_to(l3).shift(DOWN * .4),
            numneg8_2.animate.next_to(l4,LEFT).shift(DOWN * .4), run_time = 0.4
        )
        
        self.play(
            m0.animate.restore(),
            signs.animate.restore(), run_time = 0.4
        )
        
        self.play(
            signs[2].animate.set_color("#58FF7A00"),
            m0[0][2].animate.set_color("#58FF7A00"), run_time = 0.4
        )
        
        plus2copy = plus2.copy()
        self.play(
            plus2copy.animate.next_to(l4).set_color(WHITE).shift(UP * .3), run_time = 0.4
            
        )
        
        copy5 = m0[0][2].copy()
        self.play(copy5.animate.next_to(plus2copy).shift(LEFT * .15).set_color(WHITE), run_time= 0.4)
        self.play(
            m0[0][0].animate.set_color("#949494FF"),
            m0[0][1].animate.set_color("#949494FF"),
            m0[0][5].animate.set_color("#949494FF"),
            m0[0][8].animate.set_color("#949494FF"), run_time = 0.4
        )
        
        l5 = line1.copy().next_to(copy5).shift(DOWN * .3 + LEFT * .1)
        l6 = line2.copy().next_to(l5,buff=2.5).shift(LEFT * .2)
        self.play(
                  FadeIn(l5,l6), run_time = 0.4
                  )
        
        numneg5_2 = m0[0][3].copy()
        num6_2 = m0[0][4].copy()
        num7_2 = m0[0][6].copy()
        num9_2 = m0[0][7].copy()
        self.play(
            numneg5_2.animate.next_to(l5).shift(UP * .4),
            num6_2.animate.next_to(l6,LEFT).shift(UP * .4),
            num7_2.animate.next_to(l5).shift(DOWN * .4),
            num9_2.animate.next_to(l6,LEFT).shift(DOWN * .4), run_time = 0.4
        )
        
        self.play(
            m0.animate.restore(),
            signs.animate.restore(), run_time = 0.4
        )
        
        detsigncopy = detsign.copy()
        self.play(detsigncopy.animate.shift(DOWN * 2 + LEFT*1.3).scale(.6), run_time = 0.4)
        
        num8copy = num8.copy()
        self.play(num8copy.animate.next_to(detsigncopy).scale(.6), run_time = 0.4)
        openbrac = Text("(").scale(1).next_to(num8copy,buff=0.1)
        self.play(FadeIn(openbrac), run_time = 0.4)
        
        num6copy = num6.copy()
        self.play(
            num6copy.animate.next_to(openbrac,buff=.1).scale(.6),run_time = 0.4
            )
        timessign = MathTex(r"\times").scale(.6).next_to(num6copy)
        self.play(
            FadeIn(timessign),run_time = 0.4
        )
        
        numneg8copy = numneg8.copy()
        self.play(
            numneg8copy.animate.next_to(timessign,buff=.1).scale(.6),run_time = 0.4
        )
        
        minus2 = minus1.copy().next_to(numneg8copy)
        self.play(Write(minus2), run_time = 0.4)
        
        brac = Text("(").scale(0.6).next_to(minus2, buff= 0.1)
        self.play(FadeIn(brac), run_time = 0.4)
        
        numneg2copy = numneg2.copy()
        self.play(numneg2copy.animate.next_to(brac,buff=.1).scale(.6), run_time = 0.4)
        
        timessign2 = timessign.copy().next_to(numneg2copy)
        self.play(FadeIn(timessign2), run_time = 0.4)
        
        num9copy = num9.copy()
        self.play(num9copy.animate.next_to(timessign2).scale(.6), run_time = 0.4)
        
        brac1 = Text(")").scale(0.6).next_to(num9copy, buff= 0.1)
        self.play(FadeIn(brac1), run_time = 0.4)
        
        closebrac = Text(")").scale(1).next_to(brac1,buff=0.1)
        self.play(FadeIn(closebrac), run_time = 0.4)
        
        migroup = VGroup(minus1copy,copy4).copy().scale(0.6)
        self.play(migroup.animate.next_to(closebrac,buff=.1), run_time = 0.4)
        
        openbrac1 = Text("(").scale(1).next_to(migroup,buff=0.1)
        self.play(FadeIn(openbrac1), run_time = 0.4)
        
        numneg5copy = numneg5.copy()
        self.play(numneg5copy.animate.next_to(openbrac1,buff = 0.1).scale(0.6), run_time = 0.4)
        
        timessign1 = MathTex(r"\times").scale(.6).next_to(numneg5copy)
        self.play(FadeIn(timessign1), run_time = 0.4)
        
        numneg8copy_2 = numneg8_2.copy()
        self.play(numneg8copy_2.animate.next_to(timessign1,buff=.1).scale(.6), run_time = 0.4)
        
        minus3 = minus1.copy().next_to(numneg8copy_2)
        self.play(Write(minus3), run_time = 0.4)
        
        brac3 = brac = Text("(").scale(0.6).next_to(minus3, buff= 0.1)
        self.play(FadeIn(brac3), run_time = 0.4)
        
        numneg2copy_2 = numneg2_2.copy()
        self.play(numneg2copy_2.animate.next_to(brac3, buff = 0.1).scale(0.6), run_time = 0.4)
        
        timessign3 = MathTex(r"\times").scale(.6).next_to(numneg2copy_2)
        self.play(FadeIn(timessign3), run_time = 0.4)
        
        num7copy = num7.copy()
        self.play(num7copy.animate.next_to(timessign3, buff=0.1).scale(0.6), run_time = 0.4)
        
        brac4 = brac = Text(")").scale(0.6).next_to(num7copy, buff= 0.1)
        self.play(FadeIn(brac4), run_time = 0.4)
        
        closebrac1 = Text(")").scale(1).next_to(brac4, buff=0.1)
        self.play(FadeIn(closebrac1), run_time = 0.4)
        
        pgroup =VGroup(plus2copy, copy5).copy().scale(0.6)
        self.play(pgroup.animate.next_to(closebrac1,buff=.1), run_time = 0.4)
        
        openbrac2 = Text("(").scale(1).next_to(pgroup, buff=0.1)
        self.play(FadeIn(openbrac2), run_time = 0.4)
        
        numneg5_2copy = numneg5_2.copy()
        self.play(numneg5_2copy.animate.next_to(openbrac2, buff=0.1).scale(0.6), run_time = 0.4)
        
        timessign4 = MathTex(r"\times").scale(.6).next_to(numneg5_2copy)
        self.play(FadeIn(timessign4), run_time = 0.4)
        
        
        num9_2copy = num9_2.copy()
        self.play(num9_2copy.animate.next_to(timessign4, buff=0.1).scale(0.6), run_time = 0.4)
        
        minus4 = minus1.copy().next_to(num9_2copy)
        self.play(Write(minus4),run_time = 0.4)
        
        num6_2copy = num6_2.copy()
        self.play(num6_2copy.animate.next_to(minus4, buff=0.1).scale(0.6),run_time = 0.4)
        
        timessign5 = MathTex(r"\times").scale(.6).next_to(num6_2copy )
        self.play(FadeIn(timessign5), run_time = 0.4)
        
        num7_2copy = num7_2.copy()
        self.play(num7_2copy.animate.next_to(timessign5, buff=0.1).scale(0.6), run_time = 0.4)
        
        closebrac2= Text(")").scale(1).next_to(num7_2copy, buff=0.1)
        self.play(FadeIn(closebrac2), run_time = 0.4)
        
        detsigncopy_1 = detsigncopy.copy()
        self.play(detsigncopy_1.animate.shift(DOWN * 1 + RIGHT*5.2).scale(2), run_time = 0.4)
        
        total_group = VGroup(num8copy, openbrac, num6copy, timessign , numneg8copy, minus2 , brac ,
                             numneg2copy , timessign2 , num9copy , brac1 , closebrac ,migroup, openbrac1 ,
                             numneg5copy,timessign1, numneg8copy_2 ,minus3 ,
                             brac3,numneg2copy_2,timessign3 ,num7copy,brac4,closebrac1,
                             pgroup ,openbrac2 ,numneg5_2copy , timessign4 , num9_2copy , minus4 ,
                             num6_2copy , timessign5, num7_2copy , closebrac2).copy()
        
        self.play(Circumscribe(total_group ))
        self.play(Circumscribe(total_group ))
        self.play(Circumscribe(total_group ))
        
        x = 8*((6 * -8)-(-2*9))-4*((- 5* -8 )-(-2 * 7))+3*((-5 * 9)-(6 * 7))
        solution = MathTex(str(x)).next_to(detsigncopy_1)
        self.play(Transform(total_group, solution), run_time = 0.4)
        
        
    
    
    
        
        self.wait(3)
   