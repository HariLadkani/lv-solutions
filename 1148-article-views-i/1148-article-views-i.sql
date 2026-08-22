/*
goal: return author_id as id
where author_id = viewer_id
sort by author_id ASC
*/
SELECT 
    DISTINCT author_id as id
FROM Views 
WHERE author_id = viewer_id
ORDER BY author_id;