
import os,json
from indexing.services.postings_linked_list import final_linked_list,Node,Postings_Linked_List

class Daat:

    def __init__(self):
        pass


    def daatAnd(query):
        result_json = {}
        num_comparisions = 0
        sorted_pairs = Daat.getSortedPairs(query)
        result,num_comparisions = Daat.merger(sorted_pairs[0],sorted_pairs[1],num_comparisions)
        for pair in range(2,len(sorted_pairs)):
            result,num_comparisions = Daat.merger([result,0],sorted_pairs[pair],num_comparisions)

        final_list = []
        while result:
            final_list.append(result.data)
            result = result.next
        result_json["num_comparisons"] = num_comparisions
        result_json["num_docs"] = len(final_list)
        result_json["results"] = final_list
        return result_json

    def daatAndSkip(query):
        result_json = {}
        num_comparisions = 0
        sorted_pairs = Daat.getSortedPairs(query)
        result,num_comparisions = Daat.mergerWithSkip(sorted_pairs[0],sorted_pairs[1],num_comparisions)
        for pair in range(2,len(sorted_pairs)):
            result,num_comparisions = Daat.mergerWithSkip([result,0],sorted_pairs[pair],num_comparisions)

        final_list = []
        while result:
            final_list.append(result.data)
            result = result.next
        result_json["num_comparisons"] = num_comparisions
        result_json["num_docs"] = len(final_list)
        result_json["results"] = final_list
        return result_json
        


    def merger(list1,list2,num_comparisions):
        result = Postings_Linked_List()
        while(list1[0] and list2[0]):
            num_comparisions+=1
            # print(list1[0].data,'-----------------',list2[0].data)
            if list1[0].data == list2[0].data:
                result.head= Postings_Linked_List.insert(result,list1[0].data)
                list1[0]=list1[0].next
                list2[0]=list2[0].next
            elif list1[0].data > list2[0].data:
                list2[0] = list2[0].next
            else:
                list1[0] = list1[0].next
        
        return result.head,num_comparisions


    def mergerWithSkip(list1,list2,num_comparisions):
        result = Postings_Linked_List()
        while(list1[0] and list2[0]):
            num_comparisions+=1
            # print(list1[0].data,'-----------------',list2[0].data)
            if list1[0].data == list2[0].data:
                result.head= Postings_Linked_List.insert(result,list1[0].data)
                list1[0]=list1[0].next
                list2[0]=list2[0].next
            elif list1[0].data > list2[0].data:
                if list2[0].second_next and list2[0].second_next.data <= list1[0].data:
                    list2[0] = list2[0].second_next
                else:
                    list2[0] = list2[0].next
            else:
                if list1[0].second_next and list1[0].second_next.data <= list2[0].data:
                    list1[0] = list1[0].second_next
                else:
                    list1[0] = list1[0].next
        
        return result.head,num_comparisions
        


    def getSortedPairs(query):
        postings_lengths_file = os.path.join(os.path.dirname(__file__), '../helpers/postings_lengths.json')
        with open(postings_lengths_file, 'r', encoding='utf-8') as json_file:
            postings_lengths_data = json.load(json_file)
        pairs = []
        for each_token in query:
            new_list = []
            # current_query_json[each_token] = final_linked_list.get(each_token,None)
            if each_token == 'epidemic' or each_token == 'pandemic':
                print(each_token)
                Postings_Linked_List.print_list(final_linked_list.get(each_token))
            new_list.append(final_linked_list.get(each_token,None))
            new_list.append(postings_lengths_data.get(each_token,None))
            pairs.append(new_list)

        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        return sorted_pairs
        


    


    