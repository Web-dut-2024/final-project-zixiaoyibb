from django.shortcuts import render, redirect
from .models import Plan
from .forms import PlanForm

def plan_view(request):
    plans = Plan.objects.filter(flag=False)  # 只显示未完成的计划
    return render(request, 'myplan/plan.html', {'plans': plans})

def finish_view(request):
    plans = Plan.objects.filter(flag=True)  # 只显示已完成的计划
    return render(request, 'myplan/finish.html', {'plans': plans})

def delete_plan(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    plan.delete()
    return redirect('plan')  # 删除后重定向回计划页面

def add_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.flag = False  # 新计划默认未完成
            plan.save()
            return redirect('plan')  # 添加完成后重定向到计划页面
    else:
        form = PlanForm()
    return render(request, 'myplan/add_plan.html', {'form': form})


def complete_plan(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    plan.flag = True  # 标记为已完成
    plan.save()
    return redirect('plan')  # 完成后重定向回计划页面
