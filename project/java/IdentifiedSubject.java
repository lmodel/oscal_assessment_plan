package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Used to detail assessment subjects that were identified by this task.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IdentifiedSubject  {

  private String subject-placeholder-uuid;
  private List<AssessmentSubject> subjects;

}