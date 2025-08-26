from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    # student_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Enrollment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class TestTable(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'abc_table'
        ordering = ['name']






# CharField -> small sized text
# TextField -> largeText
# IntegerFiedl -> int Values
# FloatFiedl