pip install django-el-pagination==3.1.0

#settings installed apps
  'el_pagination',


#templates before for loop ( {% for instance in instances %} ) add -->
  {% load el_pagination_tags %}
  {% paginate 21 instances %} # 21 is the number of elements that should be loaded in a page


#add widget after table container
  <!--pagination -->
    {% get_pages %}
      <div class="pagination">
        {% show_pages %}
      </div>
  <!--pagination-->
  
  
#add css for pagination - 
  div.pagination{
    display: flex;
    flex-direction: row;
    justify-content: center;align-items: center;
  }
  div.pagination span.endless_page_current{
    display: inline-block;
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: linear-gradient(to right, #7eb244, #43C6AC);
    border: 1px solid #afafaf;
    color: #fff;
    padding: 13px 0;
    margin: 0 2.5px;
    box-sizing: border-box;
  }
  div.pagination a.endless_page_link{
    display: inline-block;
    width: 40px;
    height: 40px;
    margin: 0 2.5px;
    border-radius: 12px;
    border: 1px solid #afafaf;
    padding: 13px 0;
    box-sizing: border-box;
  }
