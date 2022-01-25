from durable.lang import *

# ruleset for grades and interest
with ruleset('grades_and_interests'):
   
    # facts for grades and interest

    @when_all((m.grade == 'A1') & (m.interest == 'build_read_world_intelligent_models') )
    def select_TAIS(c):
        c.assert_fact('courses',{'subject': 'AI'})
        c.assert_fact('extracurricular_activities',{'activity': 'reading_novels_and_writing_blogs'})
        c.assert_fact({'select_course': 'Select elective course as  Human Centered AI','select_activity': 'Join the courses on content writing(coursera)'})

    @when_all((m.grade == 'A2') & (m.interest == 'build_models') )
    def select_ML(c):
        c.assert_fact('courses',{'subject': 'ML'})
        c.assert_fact('extracurricular_activities',{'activity': 'making food'})
        c.assert_fact({'select_course': 'Select course as  Advanced Deep Learning','select_activity': 'Join FooBar Club'})

    @when_all((m.grade == 'A2') & (m.interest == 'design_algorithms') )
    def select_ADA(c):
        c.assert_fact('courses',{'subject': 'ADA'})
        c.assert_fact('extracurricular_activities',{'activity': 'photography'})
        c.assert_fact({'select_course': 'Select course as  Algorithms in Bioformatics','select_activity': 'Join Photography Club'})

    @when_all((m.grade == 'B2') & (m.interest =='computer security') )
    def select_NS(c):
        c.assert_fact('courses',{'subject': 'network security'})
        c.assert_fact('extracurricular_activities',{'activity': 'singing'})
        c.assert_fact({'select_course': 'Select course as  Introduction to Blockchain and Cryptocurrency','select_activity': 'Join Singing Club'})

    @when_all((m.grade == 'B2') & (m.interest == 'object_detection_and_segmentation') )
    def select_CV(c):
        c.assert_fact('courses',{'subject': 'Computer Vision'})
        c.assert_fact('extracurricular_activities',{'activity': 'python programming'})
        c.assert_fact({'select_course': 'Select course as  Advanced Computer Vision','select_activity': 'Join the courses on python programming(coursera)'})

    @when_all((m.grade == 'B1') & (m.interest == 'interference_between_hardware_and_user') )
    def select_OS(c):
        c.assert_fact('courses',{'subject': 'Operating System'})
        c.assert_fact('extracurricular_activities',{'activity': 'c programming'})
        c.assert_fact({'select_course': 'Select course as  Advanced Operating Systems','select_activity': 'Join the courses on c programming(coursera)'})


    # display output for chosen course and activity

    @when_all(+m.select_course)
    def display_course(c):
        print('Fact {0}'.format(c.m.select_course))

    @when_all(+m.select_activity)
    def display_activity(c):
        print('Fact {0}'.format(c.m.select_activity))


# ruleset for course
with ruleset('courses'):
   
    # facts for courses

    @when_all((m.subject == 'AI'))
    def select_sub(c):
        c.assert_fact({'select_course': 'take course on Trustworthy AI'})
        c.assert_fact({'select_course': 'take course on Meta Learning'})

    @when_all((m.subject == 'ML'))
    def select_sub(c):
       c.assert_fact({'select_course': 'take course on Deep Learning'})
       c.assert_fact({'select_course': 'take course on Advanced Machine Learning'})
       c.assert_fact({'select_course': 'take course on Bayesian Machine Learning'})

    @when_all((m.subject == 'ADA'))
    def select_sub(c):
       c.assert_fact({'select_course': 'take course on Modern Algorithm Design'})
       c.assert_fact({'select_course': 'take course on Introduction to Graduate Algorithms'})
       c.assert_fact({'select_course': 'take course on Randomized Algorithms'})

    @when_all((m.subject == 'network security'))
    def select_sub(c):
       c.assert_fact({'select_course': 'take course on Foundation Computer Security'})
       c.assert_fact({'select_course': 'take course on Netwroks and System Security II'})
       c.assert_fact({'select_course': 'take course on Applied Cryptography'})

    @when_all((m.subject == 'Computer Vision'))
    def select_sub(c):
       c.assert_fact({'select_course': 'take course on Image Analysis'})
       c.assert_fact({'select_course': 'take course on Digital Image Processing'})
       c.assert_fact({'select_course': 'take course on Digital Signal Processing'})

    @when_all((m.subject == 'Operating System'))
    def select_sub(c):
       c.assert_fact({'select_course': 'take course on Networks and System Security II'})
       c.assert_fact({'select_course': 'take course on Security Engineering'})
       c.assert_fact({'select_course': 'take course on Parallel Runtimes for Modern Processors'})


    # display output for chosen course
    @when_all(+m.select_course)
    def output(c):
        print('Fact {0}'.format(c.m.select_course))

# ruleset for extracurricular activities
with ruleset('extracurricular_activities'):
    
    # facts for extracurricular activities

    @when_all((m.activity == 'making food'))
    def select_act(c):
        c.assert_fact({'select_activity': 'take activity as Cooking'})

    @when_all((m.activity == 'reading_novels_and_writing_blogs'))
    def select_act(c):
        c.assert_fact({'select_activity': 'take activity as blog writer'})
        c.assert_fact({'select_activity': 'take activity as freelencer writer'})
        c.assert_fact({'select_activity': 'take activity as content writer'})

    @when_all((m.activity == 'photography'))
    def select_act(c):
        c.assert_fact({'select_activity': 'take activity as food photography'})
        c.assert_fact({'select_activity': 'take activity as wildlife photography'})
        c.assert_fact({'select_activity': 'take activity as nature photography'})

    @when_all((m.activity == 'singing'))
    def select_act(c):
        c.assert_fact({'select_activity': 'take activity as vocalist'})

    @when_all((m.activity == 'python programming'))
    def select_act(c):
        c.assert_fact({'select_activity': 'take activity as Cooding in Python language'})

    @when_all((m.activity == 'c programming'))
    def select_act(c):
        c.assert_fact({'select_activity': 'take activity as Cooding in C language'})


    # display output for chosen activity
    @when_all(+m.select_activity)
    def display(c):
        print('Fact {0}'.format(c.m.select_activity))
        
      
assert_fact('grades_and_interests', { 'grade': 'B2', 'interest': 'object_detection_and_segmentation' })
#assert_fact('grades_and_interests', { 'grade': 'A1', 'interest': 'build_read_world_intelligent_models' })
#assert_fact('grades_and_interests', { 'grade': 'A2', 'interest': 'build_models' })
#assert_fact('grades_and_interests', { 'grade': 'A2', 'interest': 'design_algorithms' })
#assert_fact('grades_and_interests', { 'grade': 'B2', 'interest': 'computer security' })
#assert_fact('grades_and_interests', { 'grade': 'B1', 'interest': 'interference_between_hardware_and_user' })
